# Binary commerce screening: next research route

Updated 2026-10-03. This is a prospective development plan.

The main task distinguishes credible drug-commerce suspicion from noncommercial content. Existing fine categories remain useful for error analysis. Records with insufficient information form a separate uncertainty cohort.

The next controlled study uses a shared Chinese MacBERT text encoder with four arms: direct CLS classification, attention pooling without auxiliary supervision, attention pooling with fixed random token supervision, and attention pooling with human evidence supervision. All arms use the same binary labels, development splits, paired seeds, and update budgets. A character TF-IDF/linear-SVM baseline provides a low-cost control. The study tests classification performance and difficult noncommercial errors; attention agreement is reported as evidence alignment.

Development proceeds through data projection and implementation checks, a bounded first-seed comparison, a fixed three-seed comparison, and separately frozen human confirmation. AI annotations, if used for workflow tests, have a separate development-only provenance record. Human evaluation labels remain independently recorded.

Regular supervision runs every 40 minutes, checks incremental artifacts and actual process logs, and reports substantive milestones. Final conclusions require completed experiments and reviewer-verifiable evidence.

Related work: [learning from rationales](https://aclanthology.org/2022.findings-acl.86/), [evaluation of explanation benchmarks](https://aclanthology.org/2024.findings-eacl.88/).
