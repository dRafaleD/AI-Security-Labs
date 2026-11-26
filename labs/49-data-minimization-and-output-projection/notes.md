# Day 49 — Data Minimization and Output Projection

[English](notes.md) · [Türkçe](notes.tr.md) · [Code](projection_demo.py)

Day 48 checked which fictional documents an assistant may read. Day 49 applies a second boundary: which fields may leave the trusted application. The output is built from a role-specific allowlist; mixed allowed and disallowed requests fail closed. Missing fields and duplicate names receive explicit errors.

**Worked cases:** a reader requesting title succeeds; a reader requesting internal_id is denied; an auditor requesting internal_id succeeds; title plus private_note is denied without returning a partial record. Eleven scenarios assert both the decision and output keys.

**Practice:** add a public role with title-only access; test an empty list and a missing field. Explain why structured field projection does not detect confidential text already embedded inside an allowed summary. Real systems must bind role and record to authenticated identity and validate content, not just keys. No actual AI, sensitive data, or tool calls.

## Run
```bash
python3 labs/49-data-minimization-and-output-projection/projection_demo.py
```
