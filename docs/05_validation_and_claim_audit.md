# Validation and research claim audit

## Before evaluation
- [ ] Freeze a train/validation/test split or an evaluation protocol.
- [ ] Ensure duplicate or near-duplicate query-document pairs do not leak across splits.
- [ ] Define metrics before tuning.
- [ ] Confirm label quality and class balance.
- [ ] Record package versions and random seeds where applicable.

## Claims audit
For each claim in the report, record the evidence that supports it.

| Claim | Evidence / file | Data split | Metric | Limitation | Safe wording? |
|---|---|---|---|---|---|
| | | | | | |

## Do not claim
- That synthetic demo scores represent real search engines.
- That the model increases clicks, traffic, revenue, or Google ranking without an appropriate real-world evaluation.
- That a model is production-ready based only on this toy demonstration.
