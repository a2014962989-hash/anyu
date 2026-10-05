# Reviewed output-sufficiency experiment results

Root independently reviewed saved predictions, original frozen metadata, all ten epoch summaries, selection, effective updates, paired batch records, binding and elapsed budgets. The final saved-output review found zero issues. Initialization, actual first-batch boundary, complete before/after RNG components and forward shapes had separately been verified equal for this new pair.

| Arm | Full development Macro-F1 (136) | Clean development Macro-F1 (133) | Clean commercial-category recall (8) | Selected epoch |
| --- | ---: | ---: | ---: | ---: |
| S0 random retained-input CE | 0.9443079443079443 | 0.9418367346938775 | 1.0 | 4 |
| S1 human-evidence retained-input CE | 0.9355668358714044 | 0.9327555074033947 | 1.0 | 4 |

Both arms completed five epochs and 360 effective optimizer/scheduler updates, with 2,860 full and 2,285 retained training-example exposures per arm. They used the same pretrained architecture and fixed weighted logical-batch objective, full CE plus 0.20 retained CE. Recorded training durations were 2,817.797 and 3,015.516 seconds; the combined budget charge was 5,833.563 seconds within the authorized cap.

S1 changed one prediction into an additional error and corrected zero errors in each development set. Its full and clean Macro-F1 decreased by 0.008741108436539857 and 0.009081227290482774 versus S0. All four prespecified minimum 0.01 gain checks against the new paired control and historical strongest controls failed. Both commercial-category recall-loss checks passed.

Root accepted the complete numerical evidence and closed this objective as CLOSED_OUTPUT_SUFFICIENCY_CE_NO_DEVELOPMENT_GAIN. There is no additional coefficient, seed, masking, threshold, epoch or loss search authorization. The earlier stopped technical candidate remains a separate historical attempt; it is not substituted into this completed pair.

Two finite Root checker corrections were preserved with their original reports: the stored development partition name, and harmless probability rounding between separately batched full/clean inference. Metadata and binary predictions matched exactly across the clean subset; research outputs and thresholds were not changed. Root did not reload models/checkpoints, rerun inference or training, or read confirmation answers during this review.

The next bounded work audits metadata component consistency and actual denominators of returned TRAIN/DEVELOPMENT codes. Their workflow provenance is still unconfirmed, so they are not accepted as independent human gold. Confirmation answers remain sealed and independent confirmation remains zero. Overall research acceptance criteria are incomplete.

Only reviewed aggregates and review-document hashes are published here. Private text, identifiers, returned labels, individual predictions, RNG states, source, authorization, models, checkpoints and returned workbooks remain local.
