# Day 27 — Refusal and Safe-Failure Regression Tests

[English](notes.md) · [Türkçe](notes.tr.md)

## Learning objective
This day explores **Refusal and Safe-Failure Regression Tests** with harmless local fixtures. The goal is to reason about controls, evidence, and limits rather than treating one output as proof.

## Core concepts
1. Keep a small table of prompts that must be refused and prompts that must be answered, and run it on every change.
2. Track both error types: missed refusals and over-refusals of harmless requests.
3. When a check fails closed, the user should see a clear safe message, not a stack trace or partial output.

## Important distinctions
- A keyword filter is a baseline that paraphrases defeat; the test table exposes that gap.
- Passing the suite means no known regression, not that the system is safe.
- Use synthetic, non-harmful prompts in the table.

## Hands-on lab
Read `refusal_tests_demo.py` before running the following from this lab folder:

~~~bash
python3 refusal_tests_demo.py
~~~


## Assignments
1. Predict which cases the keyword filter gets wrong.
2. Run the demo and record the missed refusal and the over-refusal.
3. Add one more paraphrase case and update the expected counts.
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
