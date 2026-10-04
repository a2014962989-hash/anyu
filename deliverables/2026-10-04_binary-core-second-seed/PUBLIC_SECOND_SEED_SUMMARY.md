# Fixed second-seed binary development comparison

Root saved-output review completed on 2026-10-04 at 04:26 UTC. Task: suspicious drug-commerce classification, using human A/B categories as positive and C/D/E as negative, with U analyzed separately. Fixed training: 572 records; full development: 136; clean development: 133.

The four arms use local MacBERT: B0 CLS classification, B1 attention pooling, P1 random same-count token supervision, and H1 human token-evidence supervision. Seed 20260913 follows the frozen seeds 20260912/13/14. Each arm completed five epochs, 360 effective optimizer and scheduler updates, and 2,860 training-example presentations. Checkpoint selection uses clean development binary Macro-F1, with earlier epoch on ties; threshold is 0.5.

| Arm | Selected epoch | Full development Macro-F1 | Clean development Macro-F1 | Development B recall |
|---|---:|---:|---:|---:|
| B0 | 4 | 0.935567 | 0.932756 | 8/8 |
| B1 | 3 | 0.935567 | 0.932756 | 8/8 |
| P1 | 4 | 0.935567 | 0.932756 | 8/8 |
| H1 | 5 | 0.934467 | 0.931509 | 7/8 |

Root independently verified all saved numeric predictions, fixed memberships and labels, confusion-matrix arithmetic, epoch selection and matching durable batch schedules. Shared full/clean records have identical thresholded classifications and probability differences at most 5.67e-7. Training time totaled 10,803.420 seconds, within the fixed budget.

P1 selects 4,724 token positions across 457 eligible training records, matching the human evidence count. Its 1,359 chance-overlapping human positions are retained in the control accounting. The complete saved position ledger matches the frozen SHA ordering and aggregate counts.

H1's clean Macro-F1 differs from each control by -0.001247. Human evidence has not improved classification in this seed. The final fixed seed will complete the planned comparison with unchanged settings; the three-seed mean-probability ensemble will then be evaluated against the frozen development criteria.

## Reviewed evidence hashes

Saved run-summary SHA256 values:

- B0: d2c95534453f46560811a897fedc8be2c92aa7c60af78f7ef38fee5889aa4e7e
- B1: 63abc9e6917a8fdb1cfc494cb0fdff29ebf6baa7892da6f9e89608dd9fa1b216
- P1: 5abb6732846215e915a8916b0b22c45a49da5d9d4449114a841fb4c8b5a44700
- H1: a47780b47efe1bbc5f373428a722639f76b35e54228fac0c85f9f7ac2916cdf2
