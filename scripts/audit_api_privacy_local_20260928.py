"""Read-only, offline audit; writes text-free evidence, never imports experiment runners."""
from pathlib import Path
import ast, csv, json, re, hashlib, collections
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT.parent / 'final/2026-09-28_api-privacy-audit'
OUT.mkdir(parents=True, exist_ok=True)
def sha(s): return hashlib.sha256(s.encode('utf-8')).hexdigest()
def fsha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def readcsv(p):
    with p.open(encoding='utf-8-sig', newline='') as f: return list(csv.DictReader(f))
patterns = {
 'mobile_candidate': r'(?<!\d)(?:\+?86[- ]?)?1[3-9]\d{9}(?!\d)',
 'email_candidate': r'[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}',
 'handle_candidate': r'(?<![\w])@[A-Za-z0-9_]{3,}',
 'url_candidate': r'https?://[^\s]+|www\.[^\s]+|(?:t\.me|telegram\.me)/[A-Za-z0-9_/-]+',
 'contact_candidate': r'(?:微信|vx|wx|v信|薇信|qq|telegram|tg|飞机)(?:号|账号|帐号|id|\s|:|：|=|-)*[A-Za-z0-9_]{4,}',
 'long_number_candidate': r'(?<!\d)\d{15,19}(?!\d)',
 'address_context_candidate': r'[\u4e00-\u9fff]{2,}(?:路|街|巷)\d+号',
}
def flags(s): return [k for k,v in patterns.items() if re.search(v,s,re.I)]
inventory=[]; hits=[]; errors=[]; seen=set(); unique=0
paths=sorted(list((ROOT/'experiments').rglob('api_events_private*.jsonl'))+list((ROOT/'outputs').rglob('api_events_private*.jsonl')))
for p in paths:
    events=[]
    for n,line in enumerate(p.read_text(encoding='utf-8-sig').splitlines(),1):
        if not line.strip(): continue
        try: events.append(json.loads(line))
        except Exception as e: errors.append({'path':str(p.relative_to(ROOT)),'line':n,'type':type(e).__name__})
    counts=collections.Counter(); timestamps=[]; mismatches=0
    for e in events:
        sig=sha(json.dumps(e,sort_keys=True,ensure_ascii=False))
        if sig not in seen: unique+=1; seen.add(sig)
        s=e.get('system_prompt',''); u=e.get('user_prompt','')
        if e.get('timestamp_utc'): timestamps.append(e['timestamp_utc'])
        if s and u and e.get('prompt_sha256') and sha(s+'\n'+u)!=e['prompt_sha256']: mismatches+=1
        fs=flags(u); counts.update(fs)
        if fs: hits.append({'log':str(p.relative_to(ROOT)),'sample_id':e.get('sample_id',''),'categories':fs})
    public=p.with_name(p.name.replace('private','public')); pe=[]
    if public.exists():
        for line in public.read_text(encoding='utf-8-sig').splitlines():
            if line.strip(): pe.append(json.loads(line))
    inventory.append({'path':str(p.relative_to(ROOT)),'sha256':fsha(p),'private_events':len(events),'public_events':len(pe),'public_status':dict(collections.Counter(e.get('status','missing') for e in pe)),'first_utc':min(timestamps) if timestamps else None,'last_utc':max(timestamps) if timestamps else None,'prompt_hash_mismatches_using_system_newline_user':mismatches,'candidate_counts_user_prompt':dict(counts),'keys':sorted(set().union(*(e.keys() for e in events)))})
# Extract only the pure prompt-construction function; no imports or network code executed.
helper=ROOT/'scripts/186_run_transaction_slanggraph_rescue_v4_final_blind.py'
tree=ast.parse(helper.read_text(encoding='utf-8-sig'))
func=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='prompts')
scope={'json':json}; exec(compile(ast.Module(body=[func],type_ignores=[]),str(helper),'exec'),scope)
base=ROOT/'experiments/tumcc_prospective_consensusroute_v1'
source=ROOT/'data/external/tumcc_prospective_challenge_v1/TUMCC_Prospective_Challenge_Model_Input_BLIND_v1.csv'
inputs={r['sample_id']:r['model_input'] for r in readcsv(source)}
clean=ROOT/'data/00_raw/tumcc/TUMCC-clean.txt'
clean_set={re.sub(r'\s+','',s) for s in clean.read_text(encoding='utf-8-sig').splitlines() if s.strip()}
details=[]; all_ids=set(); sets=[]
for policy in ['prediction','entropy_prediction']:
    folder=base/policy; events=[json.loads(s) for s in (folder/'api_events_private.jsonl').read_text(encoding='utf-8-sig').splitlines() if s.strip()]
    ids={e['sample_id'] for e in events}; sets.append(ids); all_ids |= ids
    manifest=json.loads((folder/'prediction_manifest_v1.json').read_text())
    matches=sum((e['system_prompt'],e['user_prompt'])==scope['prompts'](inputs[e['sample_id']],[]) for e in events)
    details.append({'policy':policy,'events':len(events),'unique_sample_ids':len(ids),'exact_prompt_reconstruction_matches':matches,'prompt_hash_matches':sum(sha(e['system_prompt']+'\n'+e['user_prompt'])==e['prompt_sha256'] for e in events),'response_hash_matches':sum(sha(e['response'])==e['response_sha256'] for e in events),'selected_calls_manifest':manifest['selected_calls'],'runner_hash_matches':fsha(ROOT/'scripts/250_run_consensusroute_v1_remote_blind.py')==manifest['code_sha256'],'prediction_hash_matches':fsha(folder/'consensusroute_predictions_LOCKED_v1.csv')==manifest['predictions_sha256'],'returned_models':dict(collections.Counter(e.get('returned_model') for e in events)),'attempts':dict(collections.Counter(e.get('attempt') for e in events))})
freeze=json.loads((ROOT/'experiments/consensusroute_v1_frozen/CONSENSUSROUTE_V1_FREEZE_MANIFEST.json').read_text())
report={'scope':'Offline local records only. Candidate regex hits are not confirmed identities. Inventory is not a complete account billing or network request ledger.','inventory':inventory,'private_events_total':sum(x['private_events'] for x in inventory),'unique_exact_event_objects':unique,'parse_errors':errors,'patterns':patterns,'candidate_hits_no_text':hits,'tumcc':{'input_rows':len(inputs),'matches_clean_after_whitespace_removal':sum(t in clean_set for t in inputs.values()),'unique_transmitted_sample_ids':len(all_ids),'policy_overlap_sample_ids':len(sets[0]&sets[1]),'sample_text_candidate_counts':dict(collections.Counter(k for sid in all_ids for k in flags(inputs[sid]))),'all_800_candidate_counts':dict(collections.Counter(k for t in inputs.values() for k in flags(t))),'policies':details,'prompt_source_hash_matches_freeze':fsha(helper)==freeze['remote_verifier']['prompt_source']['sha256'],'remote_config':freeze['remote_verifier'],'input_sha256':fsha(source),'clean_sha256':fsha(clean)}}
report['verification_passed'] = (not errors and all(x['prompt_hash_mismatches_using_system_newline_user']==0 for x in inventory) and all(x['events']==x['exact_prompt_reconstruction_matches']==x['prompt_hash_matches']==x['response_hash_matches']==x['selected_calls_manifest'] and x['runner_hash_matches'] and x['prediction_hash_matches'] for x in details) and report['tumcc']['prompt_source_hash_matches_freeze'])
assert report['verification_passed'], 'Evidence verification failed'
(OUT/'audit_evidence_textfree.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in report.items() if k not in ('inventory','candidate_hits_no_text','patterns')},ensure_ascii=False,indent=2))
print('LOG_SUMMARIES')
for x in inventory: print(json.dumps({k:x[k] for k in ['path','private_events','public_status','candidate_counts_user_prompt','prompt_hash_mismatches_using_system_newline_user']},ensure_ascii=False))
