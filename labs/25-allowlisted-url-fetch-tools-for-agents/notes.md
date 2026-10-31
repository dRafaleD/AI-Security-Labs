# Day 25 — Allow-Listed URL Fetch Tools for Agents

[English](notes.md) · [Türkçe](notes.tr.md)

## Learning objective
This day explores **Allow-Listed URL Fetch Tools for Agents** with harmless local fixtures. The goal is to reason about controls, evidence, and limits rather than treating one output as proof.

## Core concepts
1. A fetch tool should accept only https URLs whose parsed host is on an allow-list.
2. Parse the URL instead of searching for substrings; `https://good.test@evil.test/` has the host `evil.test`.
3. Re-check the policy on every redirect target, because a trusted host can redirect elsewhere.

## Important distinctions
- An allow-list limits where the agent reaches; it does not make the fetched content trustworthy.
- Internal addresses need a separate block even if a hostname resolves to them.
- Fetched text is data and must never be treated as instructions for the agent.

## Hands-on lab
Read `fetch_policy_demo.py` before running the following from this lab folder:

~~~bash
python3 fetch_policy_demo.py
~~~


## Assignments
1. Predict which of the five URLs are allowed.
2. Run the demo and record the reason for each rejection.
3. Add a redirect chain and check each hop.
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
