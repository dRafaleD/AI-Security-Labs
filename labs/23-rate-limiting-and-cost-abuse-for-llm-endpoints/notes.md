# Day 23 — Rate Limiting and Cost Abuse for LLM Endpoints

[English](notes.md) · [Türkçe](notes.tr.md)

## Learning objective
This day explores **Rate Limiting and Cost Abuse for LLM Endpoints** with harmless local fixtures. The goal is to reason about controls, evidence, and limits rather than treating one output as proof.

## Core concepts
1. A token bucket allows short bursts but caps the sustained rate per user.
2. Charge requests by cost (for example input size), not only by count, so one huge prompt cannot drain the budget.
3. Limit per identity, not per IP alone, and fail closed when the limiter state is unavailable.

## Important distinctions
- Rate limits reduce abuse and bills; they do not stop prompt injection or data leakage.
- A limit that is too tight harms legitimate users; tune it from observed usage.
- Return a clear 429 with a retry hint instead of silently dropping requests.

## Hands-on lab
Read `bucket_demo.py` before running the following from this lab folder:

~~~bash
python3 bucket_demo.py
~~~


## Assignments
1. Predict how many of the ten rapid requests are allowed.
2. Run the demo and record which requests are rejected.
3. Increase the cost of each request to 5 and describe the effect.
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
