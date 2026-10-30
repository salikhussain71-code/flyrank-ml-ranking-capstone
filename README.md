# SearchRank Lab — FlyRank Machine Learning Capstone Workspace

> **Status:** starter implementation and evidence workspace. This is not a claim that FlyRank has accepted any assignment or capstone.

A reproducible, small-scale search-ranking experiment for learning how to define a ranking task, establish a baseline, evaluate ranking quality, inspect the top results, and turn findings into a documented action plan.

## Important integrity note
The FlyRank portal lists the capstone **Google Search Ranking & Discoverability Capstone** and its own resources/rubric. Read those instructions first. This repository is a transparent project scaffold; it does not replace required FlyRank resources, datasets, assignment forms, or submissions. The included dataset is synthetic demonstration data, not Google Search Console data and not real search performance evidence. Replace it only with data you are permitted to use and document its provenance.

## What is included
- `data/demo_queries.csv`: clearly labelled synthetic query/page examples.
- `src/`: baseline scoring and ranking metrics (Precision@k, Recall@k, MRR, NDCG@k).
- `scripts/run_experiment.py`: runs the baseline and saves ranked results and metrics.
- `docs/`: research question, data contract, validation plan, claim audit, action playbook, and paper outline templates.
- `evidence/assignments/`: evidence checklist/templates for the ten ML assignments.
- `tests/`: unit tests for ranking metrics.

## Requirements
- Python 3.10 or newer
- `pip`

## Windows setup (PowerShell)
```powershell
# 1. Open this folder in VS Code or PowerShell.
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```
If PowerShell blocks activation, use this for the current terminal only:
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```
Or skip activation and run `.venv\Scripts\python.exe` directly.

## Run the demonstration
```powershell
python scripts/run_experiment.py
python -m unittest discover -s tests -v
```
Outputs are written to `outputs/`. The script reports metrics on the synthetic demo dataset only.

## Data format
`data/demo_queries.csv` columns:
- `query_id`: query identifier
- `query`: example search query
- `document_id`: page/document identifier
- `title`: page title
- `snippet`: short page description
- `relevance`: demonstration relevance label (0 = not relevant, 1 = relevant)

For a real experiment, define labels before testing, document who/what produced them, avoid leakage between train/validation/test data, and follow the FlyRank data contract and capstone brief.

## Reproducibility checklist
1. Record Python and package versions.
2. Preserve the original data and its source/license.
3. Define the evaluation split before model tuning.
4. Compare against a simple baseline.
5. Report per-query and aggregate metrics, including limitations.
6. Do not report synthetic-demo results as real-world results.
7. Save commands, outputs, and dated evidence for review.

## Suggested repository workflow
Commit in small steps, for example:
- `docs: define research question and data contract`
- `feat: add baseline ranking model and metrics`
- `test: cover ranking metrics`
- `docs: add validation and claim audit`
- `docs: write capstone report and action playbook`

## License and data
No third-party dataset is bundled. The synthetic demo rows are for code testing and illustration only. Check the FlyRank brief before adding any external dataset, logo, or branded assets.
