# Day 50 — Output Schema Validation and Safe Abstention

[English](notes.md) · [Türkçe](notes.tr.md) · [Code](output_gate.py)

Day 49 minimized retrieved data. Now validate an invented summary response before display: exactly two fields, a bounded string and a reference selected from the host's allowed set. Reject duplicate keys, unknown references and extra action fields. A structurally valid response is still only data: reference membership does not prove that its summary is supported or truthful. Run the 12 cases; add a missing field, an overlong summary and an allowed reference with an inaccurate claim. Explain why the last case requires independent semantic verification. No LLM, real documents, or tool execution.

## Run
```bash
python3 labs/50-output-schema-validation-and-safe-abstention/output_gate.py
```
