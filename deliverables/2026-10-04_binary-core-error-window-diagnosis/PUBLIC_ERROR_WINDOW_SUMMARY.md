# Fixed error/window diagnosis

Root independently checked saved numeric outputs on 2026-10-04 at 11:10:10 UTC. Four frozen inputs, row joins, original prediction values, fixed error membership, category counts, length bins and support-retention counts had zero mechanical discrepancies. No model, tokenizer or fit was run for the audit.

| Original use | N | Body truncated | Support tokens lost | Eligible for auxiliary loss |
|---|---:|---:|---:|---:|
| Training | 572 | 0 | 0 | 457 |
| Full development | 136 | 0 | 0 | 111 |
| Clean development | 133 | 0 | 0 | 109 |
| Fixed clean error union | 7 | 0 | 0 | 5 |
| Remaining clean records | 126 | 0 | 0 | 104 |

The seven-case error union comprises A=3, D=1 and E=3. All three A false negatives shared by all four arms have no observed body truncation or support loss. Five cases are errors shared by all arms, one only by the three controls, and one only by H1.

**Decision: close the current window-truncation explanation for these seven observed errors.** These records do not support adding a multiwindow model to address that explanation. The previous uniform-token human-attention KL candidate remains closed. The completed twelve neural fits and one SVM fit are unchanged.

The saved numeric result was accepted independently; execution deviations and failed mechanical attempts remain in the local audit record. Numerical acceptance is separate from complete execution-contract compliance. Auxiliary eligibility is a mechanical field, not a semantic sufficiency rating.

The next bounded development task freezes twenty original training records to inspect object, commerce, relation and discourse roles as AI_DEV_ONLY annotations. This is a hypothesis check, not additional training or confirmation gold.

Root numeric QA SHA256: bf0c15cd49a6efb313759c284924d063c6725567954680d2b8c48e0fe70a28e2. Private text, IDs, human labels, predictions, evidence quotations, control positions and models are excluded from this archive.
