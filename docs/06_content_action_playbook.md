# Content action playbook — evidence-first template

Translate ranking errors into actions only when supported by actual reviewed examples.

| Observed failure | Evidence | Proposed content/search action | Expected effect | How to test | Confidence |
|---|---|---|---|---|---|
| Relevant page is not surfaced for a query | Query ID + ranked output | Clarify title/snippet or improve candidate retrieval | To be tested | Re-run held-out evaluation | Low until tested |

## Guardrails
- Do not recommend keyword stuffing, misleading titles, or fabricated content.
- Separate model/retrieval problems from content-quality problems.
- Mark every recommendation as a hypothesis until evaluated.
- Match the actual FlyRank prompt and any official guidance.
