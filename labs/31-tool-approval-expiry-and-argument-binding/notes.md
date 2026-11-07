# Day 31 — Tool Approval Expiry and Argument Binding

[English](notes.md) · [Türkçe](notes.tr.md) · [Practice](approval_demo.py)

## Learning objective

Learn the trust and evidence boundaries of **Tool Approval Expiry and Argument Binding** using harmless local fixtures.

## Core concepts

1. Human approval should be bound to a specific action, its arguments and a deadline; a generic yes is insufficient for sensitive actions.

2. Approvals must expire or be consumed to prevent replay. Changing arguments after approval requires fresh authorization.

3. Authorization checks must run outside a language model; this offline demo uses no model and no real tools.

## Safe hands-on

Read the code and predict its output before running:

```bash
python approval_demo.py
```

Output is synthetic; no operations are sent to a live target.

## Assignments

1. Identify input provenance and untrusted fields.
2. Add and test a negative or boundary case.
3. Separate direct observations from interpretations.
4. Describe additional validation needed in a real environment.

## Knowledge check

- Is any single indicator sufficient?
- What can cause false positives or missing evidence?
- What inputs are needed to reproduce the result?

## Safety and limitations

No live malware, cloud accounts, system modifications, or outbound traffic. This minimal model is not an exact platform implementation.
