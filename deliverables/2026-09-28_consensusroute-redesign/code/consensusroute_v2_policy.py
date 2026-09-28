"""Offline candidate routing policy. No labels, texts, or network calls required.

Margin measures threshold proximity, not calibrated probability of correctness.
Freeze policy on development data before evaluating a new untouched test set.
"""
import argparse
import csv
import json
import math
from pathlib import Path


def margin(p, threshold):
    if not math.isfinite(p) or not 0 <= p <= 1:
        raise ValueError('Probability must be finite and in [0,1]')
    if not 0 < threshold < 1:
        raise ValueError('Threshold must be in (0,1)')
    return (p-threshold)/(threshold if p < threshold else 1-threshold)


def route(rows, budget, macbert_threshold=.29, roberta_threshold=.21,
          review_margin=.25):
    """Global batch budget, uncertainty ranked; ties use sample_id.

    Review margin is an unvalidated operational candidate setting.
    Disagreements have priority; remaining slots serve boundary agreements.
    """
    if isinstance(budget, bool) or not isinstance(budget, int) or budget < 0:
        raise ValueError('budget must be a nonnegative integer')
    if not 0 <= review_margin <= 1:
        raise ValueError('review_margin must be in [0,1]')
    allowed = {'sample_id', 'macbert_probability', 'roberta_probability'}
    output, seen = [], set()
    for row in rows:
        if set(row) != allowed:
            raise ValueError('Input must contain exactly the three label-free fields')
        sid = str(row['sample_id'])
        if not sid.strip() or sid in seen:
            raise ValueError('sample_id must be nonempty and unique')
        seen.add(sid)
        pm, pr = float(row['macbert_probability']), float(row['roberta_probability'])
        mm, mr = margin(pm, macbert_threshold), margin(pr, roberta_threshold)
        pred_m, pred_r = int(pm >= macbert_threshold), int(pr >= roberta_threshold)
        proximity = min(abs(mm), abs(mr))
        disagree = pred_m != pred_r
        eligible = disagree or proximity <= review_margin
        output.append(dict(sample_id=sid, local_prediction=pred_r,
                           disagreement=disagree, margin=proximity,
                           eligible=eligible, selected=False,
                           status='review_budget_exhausted' if eligible else 'local_consensus'))
    ranked = sorted((r for r in output if r['eligible']),
                    key=lambda r: (not r['disagreement'], r['margin'], r['sample_id']))
    for row in ranked[:budget]:
        row['selected'] = True
        row['status'] = 'review_verifier_pending'
    return output


def semantic_decision(response):
    """Validate an offline structured verifier answer; uncertainty stays review.

    `current_commercial_act` means the present message offers, seeks, or
    facilitates commerce. Reporting or warning about another person's offer
    does not by itself establish this act. No confidence-score override.
    This function checks schema, not the truth of the answer or its evidence.
    """
    if set(response) != {'target', 'current_commercial_act', 'evidence'}:
        return None
    if response['target'] not in {'in_scope', 'out_of_scope', 'uncertain'}:
        return None
    if response['current_commercial_act'] not in {'yes', 'no', 'uncertain'}:
        return None
    if not isinstance(response['evidence'], str) or not response['evidence'].strip():
        return None
    if response['target'] == 'out_of_scope' or response['current_commercial_act'] == 'no':
        return 0
    if response['target'] == 'in_scope' and response['current_commercial_act'] == 'yes':
        return 1
    return None


def apply_verifications(routed, responses):
    """Apply supplied offline answers only to selected items; no API calls.

    Final binary predictions retain the local fallback for complete-denominator
    scoring. Review status must also be reported; never discard review cases.
    """
    selected = {r['sample_id'] for r in routed if r['selected']}
    if not set(responses).issubset(selected):
        raise ValueError('Verifier responses must belong to selected items')
    output = []
    for original in routed:
        row = dict(original, final_prediction=original['local_prediction'])
        if row['sample_id'] in responses:
            response = responses[row['sample_id']]
            decision = semantic_decision(response) if isinstance(response, dict) else None
            if decision is None:
                row['status'] = 'review_ambiguous_or_invalid_verifier'
            else:
                row['final_prediction'] = decision
                row['status'] = 'verifier_decision'
        output.append(row)
    return output


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', required=True)
    parser.add_argument('--output', required=True)
    parser.add_argument('--budget', type=int, required=True)
    parser.add_argument('--responses', help='Optional offline JSON: sample_id -> structured response')
    parser.add_argument('--macbert-threshold', type=float, default=.29)
    parser.add_argument('--roberta-threshold', type=float, default=.21)
    parser.add_argument('--review-margin', type=float, default=.25)
    args = parser.parse_args()
    with open(args.input, encoding='utf-8-sig', newline='') as handle:
        rows = list(csv.DictReader(handle))
    results = route(rows, args.budget, args.macbert_threshold,
                    args.roberta_threshold, args.review_margin)
    if args.responses:
        with open(args.responses, encoding='utf-8') as handle:
            results = apply_verifications(results, json.load(handle))
    destination = Path(args.output)
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open('w', encoding='utf-8', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=list(results[0]) if results else
                               ['sample_id','local_prediction','disagreement','margin','eligible','selected','status'])
        writer.writeheader()
        writer.writerows(results)
    print(json.dumps({'rows':len(results), 'budget':args.budget,
                      'selected':sum(r['selected'] for r in results),
                      'network_calls':0, 'status':'UNVALIDATED_CANDIDATE'}, ensure_ascii=False))


if __name__ == '__main__':
    main()
