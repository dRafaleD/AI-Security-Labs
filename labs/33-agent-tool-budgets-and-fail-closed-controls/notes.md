# Day 33 — Agent Tool Budgets and Fail-Closed Controls

[English](notes.md) · [Türkçe](notes.tr.md) · [Offline policy model](budget_guard_demo.py)

## Why a permitted tool can still be risky
Day 32 required authorization **for every step** in an agent's plan. There is another question: even if each individual call is allowed, what stops an agent loop from making thousands of calls, exhausting quota, or repeatedly touching sensitive resources?

A tool controller should apply more than a yes/no tool allowlist. Combine **principal/resource authorization**, **maximum calls**, and a **cost or token budget**. Never trust the model's own claim that it is within budget. The **application controller**, not the LLM, should enforce it.

## Control design
This deterministic exercise uses a fictional `own-notes` resource and two read-only tool names:
- `search_index` costs 2 budget units.
- `read_document` costs 1 budget unit.
- `export_data` is not allowed.
- The session has at most **2 accepted calls** and **3 total cost units**.

Checks happen **before** any count is spent. Denied calls do not consume the teaching model's budget. A real service may additionally rate-limit denied requests to avoid a free denial-flood loophole.

`BudgetGuard.authorize()` returns a decision only. **It never executes a tool.** The example separates policy decisions from side effects so a model-generated plan cannot implicitly perform work.

## Local lab
```bash
python3 budget_guard_demo.py
```
Expected decisions: allowed search, allowed read, denied third search (call limit), denied export (tool policy), denied read of someone else's resource (scope check). Assertions confirm outcomes.

## Investigation
1. Why is a total cost budget different from a call-count budget?
2. What changes if an attacker induces repeated denied actions?
3. Add a `max_cost=2` case. Which otherwise valid call must be rejected?
4. Explain why `check → increment → execute` needs atomic reservation under concurrency.
5. What do retries, cancellation, refunds and crash recovery mean for quota correctness?
6. Which fields should an audit log contain without recording unnecessary personal content?

## Boundaries
No LLM, network, real file access or tool execution is involved. Production controls must bind budgets to an authenticated principal, session/tenant, resource identity and durable shared accounting; also guard **per-call output size**, timeouts and external-provider billing.
