# Fixed third-seed binary development comparison

Root saved-output review completed on 2026-10-04 at 08:26 UTC. Task: suspicious drug-commerce classification, with human A/B categories positive and C/D/E negative; U is analyzed separately. Fixed training: 572 records; full development: 136; clean development: 133.

The four MacBERT arms are B0 CLS classification, B1 attention pooling, P1 random same-count token supervision, and H1 human token-evidence supervision. Seed 20260914 completes the frozen seeds 20260912/13/14. Each arm completed five epochs, 360 effective optimizer and scheduler updates, and 2,860 training-example presentations. Checkpoint selection uses clean development binary Macro-F1, with earlier epoch on ties; threshold is 0.5.

| Arm | Selected epoch | Full development Macro-F1 | Clean development Macro-F1 | Development B recall |
|---|---:|---:|---:|---:|
| B0 | 2 | 0.924444 | 0.920974 | 7/8 |
| B1 | 4 | 0.944308 | 0.941837 | 8/8 |
| P1 | 4 | 0.934467 | 0.931509 | 8/8 |
| H1 | 2 | 0.944308 | 0.941837 | 8/8 |

Root independently verified all saved numeric predictions, fixed memberships and labels, confusion-matrix arithmetic, epoch selection and matching durable batch schedules. Shared full/clean records have identical thresholded classifications and probability differences at most 2.39e-6. Third-seed training time totaled 11,316.530 seconds, within the fixed budget. All twelve planned neural runs are complete.

P1 selects 4,724 token positions across 457 eligible training records, matching the human evidence count. Its 1,374 chance-overlapping human positions are retained in the control accounting. The complete saved position ledger matches the frozen SHA ordering and aggregate counts.

H1 matches B1 in this seed and was below B1 in the first two seeds. Human evidence has not shown a consistent classification advantage over the matched attention-pooling control. The fixed three-seed mean-probability ensemble analysis will evaluate all arms against the original development criteria.

## Reviewed evidence hashes

Saved run-summary SHA256 values:

- B0: d22cd972a7a7b042e854584307c59a73745ae7046b90b45d6ac0204d37f3c4e6
- B1: 6e0f88f14e7e1912c13bb0bc5bf37a758a39df39d8bc7540a5a3fa4cb91aa833
- P1: e03d35835f806eaa04e7cff54a60da733071a4ba02063b471f61e4985ae4375b
- H1: ddd96423fbd7ff26c45e4f47de778d4b08fa89ed29febd87c293cfae9d8c8723
