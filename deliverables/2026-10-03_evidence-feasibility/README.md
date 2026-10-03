# Evidence feasibility: reviewed research snapshot

This bundle records completed local preflights and closed branches, as of 2026-10-03 UTC. It supersedes older repository status for the current v7 evidence study. It contains aggregate counts and a data-independent geometry core. Private text, record identifiers, annotation books, per-record diagnostics, prompts and model weights remain local.

## Files

- SUMMARY.json: accepted annotation counts, data gates and measured geometry feasibility.
- PROTOCOL.md: fixed geometry rule, input contract and decision limits.
- geometry_core.py: three function bodies extracted unchanged from the reviewed execution script; no tokenizer, model or data loader.
- PUBLIC_FILES_SHA256.json: byte counts and hashes for these public artifacts.

## Results and decision

775 formal human annotations and 60 calibration annotations were accepted. Original data fail fixed D and B count gates. The single 50-record supplement also fails the clean-development B gate even at its optimistic upper bound of 9 against a requirement of 10. Both training branches are closed.

Human evidence usability passes the original coverage gate (452/572 training AE records). The stricter matched-complement geometry succeeds for only 145/572 records in each seed, below the required 229. A/B/C/D each fail the 20% class gate; E passes. This input branch is closed. These are feasibility failures before model training, not measured model-effect failures. No new neural training, neural forward, SVM fit or GPU experiment was performed; independent confirmation remains zero.

The geometry core was statically reviewed against the execution source. This public export was not rerun on private data. Aggregate diagnostics were independently reaggregated locally from saved outputs. The full private preflight also checks offsets, truncation, rationale completeness and agreement of five hypothesis body windows; this export alone does not implement that pipeline.

GitHub synchronization uses the existing anyu repository. Commit identity is available in repository history; older local unpushed commits are preserved outside this synchronization branch. Overall research and submission acceptance remain incomplete.
