# Day 30 — Agent Memory Write Policy and Poisoning Checks

[English](notes.md) · [Türkçe](notes.tr.md)

## Learning objective
This day explores **Agent Memory Write Policy and Poisoning Checks** with harmless local fixtures. The goal is to reason about controls, evidence, and limits rather than treating one output as proof.

## Core concepts
1. Persistent agent memory is an input to every future conversation, so a bad write keeps working long after the original chat ends.
2. Allow writes only from user-confirmed facts and reject text that reads like an instruction to the agent.
3. Store the source and time of each memory so a suspicious entry can be traced and removed.

## Important distinctions
- A filter for instruction-like text is a baseline; paraphrases can pass.
- Content fetched from tools or web pages is never a user-confirmed fact.
- Let users view and delete what the agent remembers.

## Hands-on lab
Read `memory_policy_demo.py` before running the following from this lab folder:

~~~bash
python3 memory_policy_demo.py
~~~


## Assignments
1. Predict which memory writes are accepted.
2. Run the demo and record the reason for each rejection.
3. Add a paraphrased instruction and describe why the filter misses it.
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
