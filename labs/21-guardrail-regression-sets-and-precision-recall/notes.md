# Day 21 — Guardrail Regression Sets, Precision and Recall

[English](notes.md) · [Türkçe](notes.tr.md)

## Learning objective
This day explores **Guardrail Regression Sets, Precision and Recall** with harmless local fixtures. The goal is to reason about controls, evidence, and limits rather than treating one output as proof.

## Core concepts
1. A guardrail should be measured on a labeled set, not judged by a few examples.
2. Precision shows how many blocks were correct; recall shows how many bad prompts were caught.
3. Benign near-misses and paraphrases are where simple rules fail; keep them in the set.

## Important distinctions
- Finding an indicator does not validate every inference about it.
- Identify the trust boundary and the party controlling each input.
- Use both positive and negative cases; document measurement limitations.

## Hands-on lab
Read `guardrail_eval.py` before running the following from this lab folder:

~~~bash
python3 guardrail_eval.py
~~~

## Assignments
1. Predict the output from the code.
2. Run the program and record inputs and outputs.
3. Change a harmless input and explain the resulting difference.
4. Add an assertion for one security property.
5. Describe a negative case and a potential false positive.
6. Propose an independent corroboration method.

## Knowledge check
1. Where does the input originate?
2. What was directly observed?
3. What assumptions might fail in production?
4. Which evidence would be insufficient?
5. What should an automated test check?

## Safety and limitations
Use only authorized systems and synthetic data. The example is not a complete security or detection product.
