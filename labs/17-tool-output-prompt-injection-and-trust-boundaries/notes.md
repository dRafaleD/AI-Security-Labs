# Day 17 — Prompt Injection in Tool Outputs and Trust Boundaries

[English](notes.md) · [Türkçe](notes.tr.md)

## Goal
Learn why retrieved pages and tool results are **untrusted data**, not instructions for an AI assistant. Explore an offline miniature agent that can summarize records but must never execute directives found inside them.

## Concepts
- **Prompt injection** attempts to turn lower-trust text into instructions that override an application's authorized workflow.
- The **data/instruction boundary** matters even when a document appears relevant or authoritative.
- Input filtering may help, but cannot prove all attacks impossible. Enforce tool permissions and output schemas outside the model.
- A model's confident wording is not evidence of authorization.
- Test both ordinary content and malicious-looking strings without invoking any actual LLM or external tool.

## Practice
```bash
python3 tool_output_boundary_demo.py
```
The script treats source text as inert content, produces a structured summary, and asserts that an embedded instruction cannot change the allowed action. This deterministic model **does not measure real LLM resistance**.

## Exercises
1. Which actor controls the retrieved text?
2. Why would following the embedded "instruction" cross a boundary?
3. Add a new adversarial string and confirm the authorized action remains unchanged.
4. Explain why schema validation and least-privilege tools still matter in an LLM product.
5. Propose a realistic evaluation with explicit attack success rates and legitimate-task success.

## Safety
Synthetic local strings only; no credentials, live services, or agent execution.
