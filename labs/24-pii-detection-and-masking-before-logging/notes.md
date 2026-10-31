# Day 24 — PII Detection and Masking Before Logging

[English](notes.md) · [Türkçe](notes.tr.md)

## Learning objective
This day explores **PII Detection and Masking Before Logging** with harmless local fixtures. The goal is to reason about controls, evidence, and limits rather than treating one output as proof.

## Core concepts
1. Mask personal data before it reaches logs, traces and analytics, because those stores are widely readable.
2. Pattern-based masking catches structured data such as emails and card-like numbers, not free-form names.
3. Keep a short non-reversible fingerprint when you need to correlate events without storing the value.

## Important distinctions
- A regex is a safety net, not a guarantee; design what you log instead of masking everything afterward.
- False positives (long numbers that are not cards) are cheaper than missed leaks.
- Test with synthetic data only; never put real personal data in fixtures.

## Hands-on lab
Read `mask_demo.py` before running the following from this lab folder:

~~~bash
python3 mask_demo.py
~~~


## Assignments
1. Predict what the masked log line looks like.
2. Run the demo and compare the fingerprints of the two emails.
3. Add a phone number pattern and test it with a synthetic number.
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
