# Fixed pilot: geometric control feasibility

The completed diagnostic evaluated 53 records using two independently returned human evidence variants and three fixed seeds. Each evidence variant and seed admitted 7/53 records under the fixed geometric control design. The prespecified overall requirement was 22/53. The candidate was therefore closed; all variants and seeds remain reported.

Each variant/seed contained 24 records with inconsistent body windows and 22 records without a recorded admissible strict complement, alongside the seven selected records. The result identifies a bottleneck in this fixed control construction. No classifier was trained in this diagnostic.

Implementation scope: the runner used a local preparation implementation rather than the frozen P2 preparation function. Its reported usable counts are implementation-specific. Closure uses the unfiltered selected-record upper bound, which is already below the requirement. The diagnostic does not establish equivalence to frozen P2 preprocessing.

The prospective binary-core study has a separate single-text-window implementation and explicit structural/random-supervision controls. It keeps this failed candidate closed.

Private texts, annotation rows, evidence intervals, and per-record diagnostics remain local. The underlying diagnostic SHA256 is `10ca899e45f37d83c8f901912f2dac8e55d9064b609e5a8c45050abe65a1a7ad`. Root's saved-result review SHA256 is `7521938f4b2ce3a6258f77e9dce85ee2ad66cb849a277979bc176e60cc52eb80`.
