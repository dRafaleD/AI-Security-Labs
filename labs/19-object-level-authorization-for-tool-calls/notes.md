# Day 19 — Object-Level Authorization for Tool Calls

[English](notes.md) · [Türkçe](notes.tr.md)

## Learning objective
This day explores **Object-Level Authorization for Tool Calls** with harmless local fixtures. The goal is to reason about controls, evidence, and limits rather than treating one output as proof.

## Core concepts
1. A tool call that passes schema validation can still reference an object the user must not see.
2. Authorize against the authenticated session user, never against an identity or role the model or prompt claims.
3. Return the same response for a missing object and a forbidden one so the model cannot probe which IDs exist.

## Important distinctions
- Schema validation answers "is this well-formed?"; authorization answers "is this caller allowed?".
- An instruction in the system prompt is guidance for the model, not an access control.
- Identify which values come from the session and which come from model output.

## Hands-on lab
Read `authz_demo.py` before running the following from this lab folder:

~~~bash
python3 authz_demo.py
~~~


## Assignments
1. Predict the three printed results before running the demo.
2. Run it and record which call returns data and which returns an error.
3. Change the session user to `bob` and explain how the results change.
4. Add an assertion that a model-supplied `owner` argument is ignored.
5. Describe a negative case where the object exists but belongs to another tenant.
6. Propose an independent check, such as a database row-level policy, that backs up the tool.

## Knowledge check
1. Where does the input originate, and who controls it?
2. What was directly observed, as opposed to inferred?
3. What assumptions might fail in production?
4. Which evidence would be insufficient on its own?
5. What should an automated test check?

## Safety and limitations
Use only authorized systems and synthetic data. The example is not a complete security or detection product.
