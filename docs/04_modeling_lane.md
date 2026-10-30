# Modeling lane — decision record template

## Candidate approaches
1. Token-overlap baseline (included).
2. TF-IDF / BM25 retrieval baseline, if compatible with the actual data and allowed dependencies.
3. A learning-to-rank model only if the dataset has enough trustworthy labelled examples and the FlyRank brief expects it.

## Selection criteria
- Performance on held-out data.
- Reproducibility and explainability.
- Data size and label quality.
- Latency and operational complexity, if relevant to the brief.
- Whether the added complexity gives a measurable improvement over baseline.

## Record your decision
- Chosen model:
- Why it matches the task:
- Baseline to beat:
- Evaluation split:
- Metric(s) chosen before tuning:
- Known risks:
- Evidence supporting the decision:
