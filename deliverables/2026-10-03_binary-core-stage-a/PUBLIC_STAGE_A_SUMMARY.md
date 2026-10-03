# Reviewed binary-core development preparation

Date: 2026-10-03. The primary task maps human categories A/B to commerce suspicion and C/D/E to noncommercial content. U remains a separate information-insufficiency queue; X follows the fixed quality exclusion. Fine categories support analysis.

## Fixed human development data

| Partition | Records | Positive | Negative |
|---|---:|---:|---:|
| Training | 572 | 164 | 408 |
| Full development | 136 | 37 | 99 |
| Clean development subset | 133 | 35 | 98 |

The accepted snapshot contains 775 records, including 66 U and one X. Partitions, human labels and evidence were retained.

## One fixed CPU baseline

Character TF-IDF, n-grams 2–5, min_df=2, max_features=50000, sublinear TF, L2 normalization; LinearSVC C=1, class_weight=balanced, random_state=20260912. One fit used the fixed training partition.

| Evaluation | Binary Macro-F1 |
|---|---:|
| Full development | 0.8627450980 |
| Clean development | 0.8559715347 |

These are development results; confirmation evaluation is a later phase.

## Evidence supervision preparation

The pure-text local MacBERT fast-tokenizer preparation uses right truncation at 256 tokens. Human evidence eligibility requires exact character intervals, complete retention of support tokens, explicit complete-rationale declaration, 1%–80% token coverage and remaining nonsupport text.

| Training group | Eligible / denominator |
|---|---:|
| All | 457 / 572 |
| Positive | 116 / 164 |
| Negative | 341 / 408 |

The fixed overall 40% and per-binary-class 20% coverage gates passed. The four implementations compare CLS, learned pooling, random same-count supervision and human evidence supervision. Eight CPU checks passed in 2.219 seconds, including logical/microbatch gradients, overflow boundaries and checkpoint recovery. Root verified the saved report's exact source/configuration bindings and local backbone hashes.

Neural fit count is zero at this snapshot. A bounded GPU technical preflight is the next authorized step; its result and formal four-arm training results are pending.

## Audit anchors

- Accepted human snapshot SHA256: `f8e1daa98c74784dffb705cd8bd41d7fc1f07b86210733e16334915a8e92ddf1`.
- Reviewed CPU-test source SHA256: `fe28672561d511966952ad48acd1e774ba745145308e970c7ca31e7ced2937a2`.
- Saved eight-check report SHA256: `85ef3a1dd3aaa32af7c88f0a144215015399137f4dffba85f0ff31e28687f44d`.

Only aggregate results and hash anchors are published here. Raw records, individual labels, evidence, predictions and model artifacts remain local.
