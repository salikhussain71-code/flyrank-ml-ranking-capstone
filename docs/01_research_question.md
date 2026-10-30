# Research question and provisional lane — draft template

## Proposed lane
Transparent baseline ranking for search-query-to-page matching.

## Research question (draft; confirm against FlyRank assignment brief)
On a small, explicitly labelled query-document dataset, how well does a simple query-token-overlap baseline place relevant pages near the top, and what failure cases should guide the next modelling step?

## Why this question is measurable
- Unit of evaluation: one query and its candidate documents.
- Ranking output: ordered documents for each query.
- Metrics: Precision@3, Recall@3, MRR, and NDCG@3.
- Error analysis: queries where a relevant document is ranked below an irrelevant one.

## Scope and limitations
The included CSV is synthetic demo data. It cannot establish claims about Google rankings, real users, search traffic, SEO outcomes, or production performance. Replace the dataset only when the official brief and data permissions allow it.

## To complete
- [ ] Paste the exact FlyRank prompt and rubric into your private working notes.
- [ ] Narrow the research question to match that prompt.
- [ ] State the intended user and decision this ranking supports.
- [ ] Define success criteria before model tuning.
- [ ] Save the submitted version and portal submission receipt.
