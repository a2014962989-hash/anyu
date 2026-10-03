# Fixed first-seed binary development comparison

Root saved-output review completed on 2026-10-03 at 23:52:20 UTC. Task: suspicious drug-commerce classification, with human A/B categories positive and C/D/E negative. U is reported separately. Fixed training set: 572 records; full development: 136; clean development: 133. The enriched 60-record source feasibility pilot is separate.

The local MacBERT experiment uses four fixed arms: B0 CLS baseline, B1 attention-pooling baseline, P1 random same-count token supervision, and H1 human token-evidence supervision. Seed 20260912 is the first of the frozen seeds 20260912/13/14. Each arm completed five epochs, 360 effective optimizer and scheduler updates, and 2,860 training-example presentations. Checkpoint selection uses clean development binary Macro-F1, with earlier epoch on ties; threshold is 0.5.

| Arm | Selected epoch | Full development Macro-F1 | Clean development Macro-F1 |
|---|---:|---:|---:|
| B0 | 4 | 0.935567 | 0.932756 |
| B1 | 5 | 0.944308 | 0.941837 |
| P1 | 5 | 0.953191 | 0.951078 |
| H1 | 3 | 0.935567 | 0.932756 |

All four arms recall the eight development B records. P1's same-count supervision has 4,724 selected token positions across 457 eligible records; its 1,372 chance-overlapping human positions are retained in the control accounting. It is a random same-count control.

Root independently checked saved numeric predictions, fixed membership/labels, confusion-matrix arithmetic, checkpoint selection and durable update schedules. Recorded full/clean probabilities differ by at most 1.61e-6 for shared records, with identical thresholded classifications. Total training time was 10,865.156 seconds, within the fixed budget.

The first-seed clean H1 difference from B1 is -0.009081 and from P1 is -0.018322. This seed provides no human-evidence advantage. The remaining two fixed seeds will complete the planned comparison without changing model, loss, parameters or labels. The three-seed ensemble and independent confirmation are pending; no submission has occurred.

## Reviewed evidence hashes

Saved run-summary SHA256 values:

- B0: b057bf71340a6ca88b41109f5dc865b8a0c8e700a8760a1f569ec4e9397e2df0
- B1: 87472e66850c05195f2f2c50648bd34371d9db9ad818fcdf1902650d1f32fc3f
- P1: 9cf9ff1f5ae77d1edf0370380745c17d3084faf9b28e79fd33a25462c064ae68
- H1: ffe8590cd5ed00fc5e16165b4da1eb1c31cdae7c027d07dbc28901acf366bf0d
