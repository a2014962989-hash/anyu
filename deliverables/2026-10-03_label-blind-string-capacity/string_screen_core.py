"""Reviewed generic string-screen functions; no dataset or runner included.
Caller provides normalized_text, normalized_chars and collections.Counter counts.
Apply the fixed >=0.80 decision to returned ratio.
"""
import difflib
import unicodedata

def norm(text):
    value=unicodedata.normalize("NFKC",text).lower()
    return "".join(ch for ch in value if not ch.isspace() and unicodedata.category(ch)[0] not in {"P","S","Z","C"})

def score_pair(a,b):
    la,lb=a["normalized_chars"],b["normalized_chars"]
    total=la+lb
    if total==0 or 5*min(la,lb)<2*total: return None,"length"
    ca,cb=a["counts"],b["counts"]
    common=sum(min(ca[ch],cb[ch]) for ch in ca.keys() & cb.keys())
    if 5*common<2*total: return None,"quick"
    score=difflib.SequenceMatcher(None,a["normalized_text"],b["normalized_text"],autojunk=False).ratio()
    return score,"ratio"
