# Fixed matched-complement geometry

Prerequisites: retain only AE training records for denominators; count U/X separately. Human evidence must satisfy the original complete-offset, rationale-completeness, all-five-hypothesis usability and 1%–80% token-coverage requirements. All five hypotheses must retain identical body token IDs and offsets. A body-window mismatch disables both auxiliary terms, while retaining full-text AE training eligibility.

1. Convert selected human evidence token ordinals to maximal contiguous fragments, indexed from zero in start order.
2. For T body tokens, each fragment start has quartile floor(4*start/T). Enumerate equal-length contiguous windows in the unannotated complement whose start belongs to the same quartile.
3. Sort each fragment's candidates by SHA256 of the UTF-8 string `20261002-evidence-placebo-v1:{seed}:{blind_id}:{fragment_index}:{start}`; start ordinal breaks ties.
4. Use deterministic depth-first backtracking for the first complete nonoverlapping combination. Count every attempted placement, including overlap rejection, against 10,000 attempts. Do not attempt placement 10,001. A complete solution on the last allowed attempt is valid.
5. Mask unselected body positions in place. Preserve sequence length, attention, hypotheses and original positions. The complement may contain unannotated genuine evidence; it is not semantically verified to be evidence-free.
6. Require paired records to comprise at least 40% of all AE training records and 20% of every class in each of the three fixed seeds. Failure disables this branch; do not relax matching or resample to pass it.

The design compares direct classification, full-text hypothesis classification, human-evidence keep supervision and matched-complement keep supervision. The latter three use matched full/keep/remove forward order and shapes; the direct classifier's separate cost must be reported. The design and geometry diagnostic do not establish a method advantage or causal faithfulness. Classification, source, seed, B recall and harmful-control gates would still require prospective data and approved experiments.
