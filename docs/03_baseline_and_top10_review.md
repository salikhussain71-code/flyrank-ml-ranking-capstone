# Baseline and top-results review — template

## Baseline
The code uses a transparent token-overlap score, weighting title matches more heavily than snippet matches. It is intentionally simple and serves as a comparison point, not a production search engine.

## Run
`python scripts/run_experiment.py`

## Review table to fill with real permitted data
| Query ID | Expected relevant page(s) | Baseline top results | Correct placements? | Failure reason | Proposed action |
|---|---|---|---|---|---|
| | | | | | |

## Required honest reporting
- State the dataset and label provenance.
- Report metrics on a pre-defined evaluation set.
- Inspect both successful and failed queries.
- Do not claim causality or real-world lift from a toy dataset.
- Keep a record of every change made after looking at validation results.
