# Day 32 — Agent Plans and Stepwise Authorization

[English](notes.md) · [Türkçe](notes.tr.md) · [Offline lab](plan_guard_demo.py)

## The central distinction
An AI agent may *propose* a multistep plan, but a generated plan is **not an authorization document**. Permission to inspect a file does not imply permission to export, email, delete or modify it. Every tool invocation should pass policy checks **at execution time**.

## What the controller must know
For each step, separate the requested **action**, **target resource**, **arguments**, **principal**, and **approval state**. Resolve which resource is being addressed before checking access; aliasing and path changes can turn a safe-looking plan into another operation. Narrow, scoped permissions are stronger than a global "the agent is trusted" flag.

## Approval is not a blanket delegation
Day 31 bound approval to a specific action and deadline. Now apply that rule to a *sequence*: a user can permit read-only analysis while withholding any export permission. Approval for one step must not be silently inherited by subsequent steps. Real systems also need concurrency-safe single-use approvals and audit logs.

## Practice — no model, no external tools
```bash
python3 plan_guard_demo.py
```

The fixture contains an authorized **read**, an unauthorized **export**, and a resource-substitution attempt. The controller returns decisions, **never executes the suggested steps**.

## Exercises
1. Identify which step is denied despite being part of the same plan.
2. Add a second authorized read-only resource. What permission changes?
3. Explain why validating the plan once is weaker than checking every tool call.
4. Consider a changed file path between approval and execution. What should happen?
5. Propose an audit record with principal, normalized resource ID, action, decision and policy version.

## Limits and safety
This is deterministic Python policy logic, not an LLM prompt-injection benchmark. It cannot prove an actual agent is secure; no network, file export or destructive action occurs.
