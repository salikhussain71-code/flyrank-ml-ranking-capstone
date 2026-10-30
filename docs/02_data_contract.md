# Search-ranking data contract — draft

## Purpose
Define what one query-document row means before training or evaluation.

## Included demo schema
| Field | Type | Meaning | Required |
|---|---|---|---|
| query_id | string | Stable query identifier | yes |
| query | string | Search query text | yes |
| document_id | string | Stable candidate document identifier | yes |
| title | string | Candidate page title | yes |
| snippet | string | Candidate page summary | yes |
| relevance | integer | Demo relevance label: 0 or 1 | yes |

## Rules to decide for real data
- Data owner, collection date, permission/license, and allowed use.
- Exact meaning of each relevance label and who assigned it.
- Whether labels are binary or graded.
- Deduplication and missing-value handling.
- Query/document grouping for train/validation/test to prevent leakage.
- Sensitive data exclusions and retention policy.
- How changes to the schema are versioned.

## Quality checks
- IDs are non-empty and stable.
- Relevance values follow the agreed label set.
- No duplicate query-document pairs unless explicitly allowed.
- Each evaluation query has candidate documents and at least one labelled relevant item, or is documented as an edge case.
- Keep the original source data immutable; save a versioned cleaned copy.

**Caveat:** This contract is a starting point, not a substitute for FlyRank's two capstone resources or assignment-specific contract requirements.
