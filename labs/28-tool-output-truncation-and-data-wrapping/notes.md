# Day 28 — Tool Output Truncation and Data Wrapping

[English](notes.md) · [Türkçe](notes.tr.md)

## Learning objective
This day explores **Tool Output Truncation and Data Wrapping** with harmless local fixtures. The goal is to reason about controls, evidence, and limits rather than treating one output as proof.

## Core concepts
1. Cap the size of tool output before it enters the model context, and mark the truncation clearly.
2. Wrap the output in a delimited data block so the model and the logs can tell it apart from instructions.
3. Escape or remove your own delimiter inside the data so the content cannot close the block early.

## Important distinctions
- Delimiters help structure; they do not stop a model from following injected text.
- Truncation can cut an important part, so log the original length.
- Treat truncated and complete outputs differently in downstream logic.

## Hands-on lab
Read `truncate_demo.py` before running the following from this lab folder:

~~~bash
python3 truncate_demo.py
~~~


## Assignments
1. Predict the length of the wrapped output.
2. Run the demo and check that the injected closing tag is neutralized.
3. Change the limit to 20 characters and describe the result.
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
