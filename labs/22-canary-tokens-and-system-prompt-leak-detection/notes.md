# Day 22 — Canary Tokens and System Prompt Leak Detection

[English](notes.md) · [Türkçe](notes.tr.md)

## Learning objective
This day explores **Canary Tokens and System Prompt Leak Detection** with harmless local fixtures. The goal is to reason about controls, evidence, and limits rather than treating one output as proof.

## Core concepts
1. A canary is a random marker placed in the system prompt; if it shows up in model output, the prompt leaked.
2. Generate a fresh canary per session so a hit identifies which conversation leaked.
3. Scan every output before it reaches the user or a tool, and block or redact on a hit.

## Important distinctions
- A canary detects verbatim leakage only; a paraphrase of the prompt passes unnoticed.
- Never rely on keeping the system prompt secret as a security control.
- Log the hit with the session ID, not the full prompt, so the log itself does not leak it.

## Hands-on lab
Read `canary_demo.py` before running the following from this lab folder:

~~~bash
python3 canary_demo.py
~~~


## Assignments
1. Predict which of the three model outputs trigger the detector.
2. Run the demo and record each result.
3. Add an output that paraphrases the prompt and explain why it is not detected.
4. Add an assertion that two sessions never share a canary.
5. Describe how an attacker could strip or alter the canary before it is printed.
6. Propose an independent control, such as output filtering on sensitive phrases.

## Knowledge check
1. Where does the input originate, and who controls it?
2. What was directly observed, as opposed to inferred?
3. What assumptions might fail in production?
4. Which evidence would be insufficient on its own?
5. What should an automated test check?

## Safety and limitations
Use only authorized systems and synthetic data. The example is not a complete security or detection product.
