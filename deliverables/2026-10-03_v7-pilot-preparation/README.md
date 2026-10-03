# Published corpus label inventory and prospective v7 pilot preparation

Reviewed on 2026-10-03 UTC. This bundle contains aggregate preparation results only.

## Published labels

The pinned author release contains 6,500 category records and 13 official label literals, each with 500 records. The previously qualified Chinese subset contains 4,439 rows, 4,383 exact string representatives and 3,428 near string components. Official `drug` supports 324 Chinese rows across 233 near components; official `benign` supports 42 rows across 42 components. Eight near components involve two official labels and remain whole.

These official labels describe the released corpus; they are not project v7 gold. String components do not establish account, event, platform or complete historical independence. Prior overlap screening compared only the current 775-record project snapshot.

## Fixed feasibility pilot metadata

A deterministic, whole-component selection prepared 60 rows across 55 components. The six fixed retrieval strata have row caps 15/15/8/7/8/7. Component ranking uses SHA256(`20261003-illicit-v7-feasibility-v1:stratum:near_component_id`), followed by greedy whole-component placement with oversize groups skipped and no cross-stratum backfill. Mixed source components are excluded; `se` remains an opaque original key.

This intentionally enriched pilot is for prospective v7 annotation and evidence-collection feasibility only. It has no train/dev/confirmation allocation, does not estimate natural prevalence and is not a model-effect experiment. Two independent blind annotation tools are being prepared for separate review; human results are not available in this bundle.

The original 775-record data gate, fixed 50-record supplement and strict N3 geometry failures remain closed. No neural forward pass, research optimizer update, SVM fit or GPU experiment was run for this preparation. Project submission readiness remains incomplete.

## Provenance and review

Author repository: https://github.com/ChaseSecurity/illicit-icl ; paper: https://arxiv.org/abs/2603.28043 . Pinned author main: `c41325b5f86fb102df37561d95aa72def4dfcbda`.

Saved no-text metadata were independently checked against fixed selection rules and all aggregate projections matched. The local preparation is limited to noncommercial academic use. This public bundle includes no source text, record IDs, annotation books, individual labels, predictions, private control maps or author facts.

See PUBLIC_AGGREGATES.json for exact reviewed counts and PUBLIC_FILES_SHA256.json for file hashes.
