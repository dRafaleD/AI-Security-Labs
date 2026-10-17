# Day 10 — Agent Approval Gates, Argument Validation and Replay Protection

[English](notes.md) · [Türkçe](notes.tr.md)

## Goal
Understand agent approval gates, argument validation and replay protection through a fully local, harmless experiment. Keep observation separate from inference.

## Core concepts
1. **tool-call requests as untrusted proposals** — document the boundary, expected behavior and limitations.
2. **allowlisted operations** — document the boundary, expected behavior and limitations.
3. **typed argument validation** — document the boundary, expected behavior and limitations.
4. **server-side authorization** — document the boundary, expected behavior and limitations.
5. **explicit approval for writes** — document the boundary, expected behavior and limitations.
6. **idempotency keys and replay prevention** — document the boundary, expected behavior and limitations.

## Procedure
The included `approval_demo.py` is a synthetic training example. From the lab directory:

```bash
python3 approval_demo.py
```

**Expected:** First attempt denied without approval; next succeeds; identical request ID is rejected as replay.

## Observations to record
Write down the machine/tool versions, exact command, input, actual output, unexpected behavior, and interpretation. Explain which results are facts and which remain hypotheses.

## Exercises
1. Run the baseline and save the observed output.
2. Change one harmless input and predict what happens before running.
3. Add a negative test and distinguish a rejection from a failure to observe.
4. Restore the original, rerun it, and explain why regression tests matter.
5. Identify two realistic false-positive explanations.
6. Identify a useful independent corroborating observation.
7. Draft a short report stating limitations explicitly.

## Review questions
1. What does tool-call requests as untrusted proposals mean, why does it matter, and what does it not guarantee?
2. What does allowlisted operations mean, why does it matter, and what does it not guarantee?
3. What does typed argument validation mean, why does it matter, and what does it not guarantee?
4. What does server-side authorization mean, why does it matter, and what does it not guarantee?
5. What does explicit approval for writes mean, why does it matter, and what does it not guarantee?
6. What does idempotency keys and replay prevention mean, why does it matter, and what does it not guarantee?
7. What would improve the confidence of your result?
8. Which regression test should be automated first?

## Ethics and scope
Use only locally generated data and infrastructure you own or are authorized to study. Findings from an individual signal are not proof of an incident.
