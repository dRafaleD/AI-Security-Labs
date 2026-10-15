# Day 7 — LLM Security Evaluations, Adversarial Test Cases and Regression Gates

[🇬🇧 English](notes.md) | [🇹🇷 Türkçe](notes.tr.md)

This hands-on day builds on earlier labs, using only local harmless training data. Verify assumptions, distinguish observation from inference, and do not treat tool output as automatic security proof.

## Learning objectives

- Security invariants
- Adversarial fixtures
- Ground truth
- Deterministic enforcement
- Evaluation metrics
- Version control
- Side-effect checks
- Regression gates

## Data flow and threat model

```text
controlled training input
        ↓
parser / evaluator / analyst
        ↓
security or evidence check
        ↓
observable result
        ↓
review assumptions and limits
```

## 1. Security invariants

Define exactly which tool actions and data accesses must be blocked by code.

**Task:** Explain which trust-boundary mistake this control prevents, with a concrete example.

## 2. Adversarial fixtures

Design labeled cases for prompt injection, cross-tenant data, tool misuse and invalid output.

**Task:** Explain which trust-boundary mistake this control prevents, with a concrete example.

## 3. Ground truth

Write expected allowed/denied outcomes before running evaluation.

**Task:** Explain which trust-boundary mistake this control prevents, with a concrete example.

## 4. Deterministic enforcement

Authorization and schema validation must be tested as code, not delegated to LLM judgments.

**Task:** Explain which trust-boundary mistake this control prevents, with a concrete example.

## 5. Evaluation metrics

Separate attack success, false positives, false negatives and rate over multiple trials.

**Task:** Explain which trust-boundary mistake this control prevents, with a concrete example.

## 6. Version control

Record model, prompt, tools, policy, temperature and dataset versions for meaningful comparisons.

**Task:** Explain which trust-boundary mistake this control prevents, with a concrete example.

## 7. Side-effect checks

An assistant might refuse in prose but still issue a forbidden tool call: test actions and logs.

**Task:** Explain which trust-boundary mistake this control prevents, with a concrete example.

## 8. Regression gates

Rerun cases after changes; these synthetic tests do not establish a real model's safety.

**Task:** Explain which trust-boundary mistake this control prevents, with a concrete example.

## Local exercise

Use only the files in this repository. This example is not a production security service.

```bash
python3 security_eval.py
```

## Test matrix

| Scenario | Expected | Reason |
|---|---|---|
| Valid training input | Accept / match | Baseline |
| Wrong owner or header | Reject / no match | Scope / structure |
| Truncated or missing field | Controlled failure | Input validation |
| Unrelated benign sample | No accidental claim | False-positive awareness |

## Exercises

1. Run and record the example.
2. Write an initial hypothesis.
3. Verify the positive case.
4. Add one negative case.
5. Add another negative case.
6. Test a boundary value.
7. Find the responsible source-level check.
8. Separate observations from inferences.
9. Change one control in a working copy.
10. Rerun the whole test matrix.
11. Document limitations.
12. Write a one-page analysis report.

## Review questions

1. What is the primary trust boundary?
2. Which inputs are untrusted?
3. What does the positive test establish?
4. What does the negative test establish?
5. What does the observed output support?
6. What does it not support?
7. Which input is the most important?
8. Give an example boundary value.
9. What is fail-closed behavior?
10. Why is the demo not production-ready?
11. Describe one potential false positive.
12. Describe one potential false negative.
13. Which fields belong in an audit log?
14. What personal data is unnecessary?
15. Why record tool versions?
16. Which regressions need retesting?

## Mini challenges

1. Add a new negative test and document its expected and actual results.
2. Break one assumption in a working copy and identify which test catches it.
3. Write a short report containing source, hash, tool version, command, observation and limitations.

## Takeaway

Measure actual behavior rather than overgeneralizing from synthetic cases. Security decisions, authorization and forensic inferences require independent checks.
