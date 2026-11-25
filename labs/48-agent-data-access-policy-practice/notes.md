# Day 48 — Practice Day: Agent Data Access Policy

[English](notes.md) · [Türkçe](notes.tr.md) · [Code](access_matrix.py)

Build a small, deny-by-default access matrix for a fictional assistant. All identities, documents and approvals are host-controlled fixtures. Enforce tenant boundaries, action allowlists, document classification, ownership and approval. The output ALLOW_DATA_ONLY does not dispatch an operation.

| Worked scenario | Expected |
|---|---|
| Alice reads own internal report | ALLOW_DATA_ONLY |
| Alice reads own restricted file without approval | NEEDS_APPROVAL |
| Bob reads Alice's restricted file with approval | DENY_RESTRICTED |
| Alice reads another tenant's file | DENY_TENANT |
| Alice requests deletion | DENY_ACTION |
| Auditor requests a summary | DENY_ROLE |

**Exercises:** Predict all 15 decisions. Add an internal document for beta and test both tenants. Add a new prohibited action and verify denial. Explain why an approval cannot replace tenant authorization. Build a paper access matrix before changing any policies.

Expected final line: 15/15 access-policy cases passed. The boolean approval is assumed to be verified externally; real applications need authenticated, action-bound grants, server-side enforcement and careful review of generated summaries. No LLM, network, or actual document access.

## Run
```bash
python3 labs/48-agent-data-access-policy-practice/access_matrix.py
```
