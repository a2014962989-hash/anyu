# Frozen three-seed binary development analysis

Root independent saved-result review completed on 2026-10-04 at 09:49 UTC. The analysis uses all selected-checkpoint predictions from seeds 20260912, 20260913 and 20260914. Each arm's ensemble is the arithmetic mean of its three probabilities, classified at 0.5. Full development has 136 records; clean development has 133. Single-seed Macro-F1 means and sample standard deviations are retained separately from ensemble Macro-F1.

| Arm | Full ensemble Macro-F1 | Clean ensemble Macro-F1 | Clean confusion matrix (true rows, predicted columns 0/1) | B recall |
|---|---:|---:|---|---:|
| B0: CLS | 0.944308 | 0.941837 | [[95,3],[3,32]] | 8/8 |
| B1: attention pooling | 0.944308 | 0.941837 | [[95,3],[3,32]] | 8/8 |
| P1: random same-count token supervision | 0.944308 | 0.941837 | [[95,3],[3,32]] | 8/8 |
| H1: human token-evidence supervision | 0.944308 | 0.941837 | [[95,3],[3,32]] | 8/8 |

H1's clean ensemble gain over each control is zero, below the frozen +0.01 criterion. Its per-seed clean Macro-F1 differences from B1 are -0.009081, -0.001247 and 0; zero of three seeds shows a strict improvement, below the required two. The maximum single-seed loss and ensemble B-recall conditions pass. A real-source comparison is not evaluable from the frozen partition metadata.

The human uniform-token KL-supervision candidate is closed for lack of development gain. The binary task and its strong controls are retained for subsequent research. No loss coefficient, threshold, label, seed or split was changed to recover the failed criteria.

Equal aggregate scores do not imply identical errors. Relative to each control, H1 corrects one record and introduces one error. Every arm has three A-category misses and three negative-category false positives on clean development. The four-arm error union contains seven records. C has no false positives among 21 records; D has only one record, so its general performance cannot be estimated. The next bounded diagnostic will examine saved window and evidence-retention information without additional training or tokenization.

The successful CPU analysis took 0.156 seconds with zero model, tokenizer, GPU or fit calls. Root independently checked all 269 full/clean ensemble records and paired errors, all 24 seed/partition metric sets, all eight ensemble metric sets, sample standard deviations and the original gates. The twelve neural runs and single SVM fit remain the complete experiment budget for this candidate.

## Reviewed evidence hashes

- Aggregate metrics and gates SHA256: 3d34c5d9450f4aa16833b54bb19447d525dde3244996e0c07b43f2cf17ca2496
- Root independent saved-analysis review SHA256: 368482398f6caf57efc56c7e3cc75cd791d6d24dc1c3c7f9c13365e55db240f2
