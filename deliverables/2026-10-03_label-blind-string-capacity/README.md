# Label-blind string-screen capacity

Reviewed aggregate snapshot, 2026-10-03 UTC. The fixed local academic diagnostic completed 12,999,978 comparisons, without reading class-label values or running a model.

| Quantity | Count |
|---|---:|
| Published category-file rows | 6,500 |
| Eligible nonempty Chinese rows | 4,439 |
| Exact normalized representatives | 4,383 |
| Internal representative pairs | 9,603,153 |
| Pairs against the current 775-record comparison set | 3,396,825 |
| Internal similarity edges | 7,834 |
| Similarity edges against that comparison set | 0 |
| String-similarity connected components | 3,428 |

The normalization is NFKC, lowercase, then removal of whitespace and Unicode P/S/Z/C categories. All unordered internal pairs and all cross-set pairs were covered. The criterion is SequenceMatcher(autojunk=False).ratio >= 0.80. Exact length and character-multiset upper bounds safely prune impossible matches. Computation took 38.375 seconds; preprocessing was recorded separately. A separate reconstruction from saved metadata and edges reproduced every component and count with zero mechanical discrepancies.

These are string components, not established author, account, platform or event groups. Zero overlap concerns only the named current comparison set. It does not establish absence of historical use, v7 labels, independent confirmation, or an experiment-ready dataset. No training, annotation or model-effect claim follows from this diagnostic.

## Provenance and scope

Upstream: [ChaseSecurity/illicit-icl](https://github.com/ChaseSecurity/illicit-icl/tree/c41325b5f86fb102df37561d95aa72def4dfcbda), associated with [Wu et al., arXiv:2603.28043](https://arxiv.org/abs/2603.28043). The category Git blob is fe472b5a0ec1451d745773d2d7fc5dc5da0a00fd. Local and Git versions were bound after CRLF/LF normalization. Source keys remain as published opaque keys; no inferred alias mapping was used. Published class labels are not substituted for this project's v7 definition.

This bundle contains only aggregate results, two generic reviewed function bodies, and provenance hashes. It grants no rights to upstream data and contains no dataset, record IDs, texts, labels, predictions, annotation books or private runner. Local academic diagnostic acceptance is distinct from data redistribution and future research authorization.

See [string_screen_core.py](string_screen_core.py) for the two unmodified scoring/normalization functions and [PROVENANCE.json](PROVENANCE.json) for the reviewed artifact hashes. Syntax was parsed; this publication did not rerun scoring or any experiment.
