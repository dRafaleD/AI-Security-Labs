# Day 12 — Tool Result Provenance, Citation Checks and Grounding

[English](notes.md) | [Türkçe](notes.tr.md)

## Objective and scope

Explore tool result provenance, citation checks and grounding with a local, harmless example. Identify trust boundaries, failure cases and environmental assumptions rather than memorizing output.

## Key observations

1. Retrieval authorization precedes evidence use.
2. A citation must support the stated claim.
3. Substring checks in this example are not semantic truth verification.

## Practical exercise

Inspect `source_check.py`, predict its behavior, then run the following commands from this directory:

```bash
python3 source_check.py
```

## Analysis tasks

1. Record baseline output and compare against your prediction.
2. Change one harmless input and repeat.
3. Verify a positive and negative scenario.
4. Describe two possible false-positive or false-negative explanations.
5. Propose an independent corroborating observation.
6. Report observations, uncertainty and a next step.

## Mini challenge

Turn the demonstration into a regression test with an assertion for the intended security property.

## Review questions

1. Where is the trust boundary?
2. Which claim is directly observed versus inferred?
3. What environmental changes affect the result?
4. How should the system handle failure?
5. Why is one finding not conclusive proof?
6. What does a regression test guarantee, and what does it not?

## Safety

Use only synthetic, local or expressly authorized targets. Training results are not proof of compromise or production readiness.
