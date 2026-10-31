# Day 26 — Model and Config Pinning with Drift Checks

[English](notes.md) · [Türkçe](notes.tr.md)

## Learning objective
This day explores **Model and Config Pinning with Drift Checks** with harmless local fixtures. The goal is to reason about controls, evidence, and limits rather than treating one output as proof.

## Core concepts
1. Pin the model version and the security-relevant settings, then compare the running config to an approved fingerprint.
2. Hash a canonical form of the config so key order and whitespace do not change the result.
3. Alert on drift and run the evaluation suite again before approving a new fingerprint.

## Important distinctions
- A matching hash proves the config is unchanged, not that the config is safe.
- Floating aliases such as `latest` make pinning meaningless; pin an exact version.
- The approved fingerprint must live outside the system that could be tampered with.

## Hands-on lab
Read `drift_demo.py` before running the following from this lab folder:

~~~bash
python3 drift_demo.py
~~~


## Assignments
1. Predict which of the three configs are flagged as drifted.
2. Run the demo and record the fingerprints.
3. Reorder keys in the approved config and confirm the fingerprint is unchanged.
4. Add an assertion for one security property.
5. Describe a negative case and a potential false positive.
6. Propose an independent corroboration method.

## Knowledge check
1. Where does the input originate, and who controls it?
2. What was directly observed, as opposed to inferred?
3. What assumptions might fail in production?
4. Which evidence would be insufficient on its own?
5. What should an automated test check?

## Safety and limitations
Use only authorized systems and synthetic data. The example is not a complete security or detection product.
