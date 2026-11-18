# Day 41 — Tool Approval, Resource Versions and TOCTOU

[English](notes.md) · [Türkçe](notes.tr.md) · [Python fixture](approval_version_demo.py)

## From Day 40
Day 40 separated RAG evidence from application-controlled tool approval. Day 41 adds a **time-of-check/time-of-use (TOCTOU)** problem: a resource could change between approval and attempted use.

## Trust boundary
An approval must be bound to an authenticated actor, tenant, action, resource and **expected resource version**. The application checks the current version **again at invocation**, alongside expiry and single-use status. This training tool can simulate a read only; a write action is rejected even with a matching approval.

The eight cases cover a stale resource version, unauthorized actor/resource, wrong action, blocked write, expired approval, valid read and replay. There are no actual file or service operations.

## Run
~~~bash
python3 labs/41-tool-approval-resource-version-and-toctou/approval_version_demo.py
~~~

## Caveat and exercises
The fixture is single-process; its version check and marking the approval as used are **not atomic**. Production systems must enforce checks, state transitions and any side effect transactionally or through equivalent safe coordination.

1. Why can a valid approval become stale before execution?
2. Why is binding the exact action and resource necessary?
3. What could happen if two workers race on the same approval?
4. Does a trustworthy source document authorize the agent to perform an action?
5. Which state must be independently auditable after approval use?

## Scope
Synthetic read-only tool gate. No LLM, external tools, network, secrets or production authorization.
