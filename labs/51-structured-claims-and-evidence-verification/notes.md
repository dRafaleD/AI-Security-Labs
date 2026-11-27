# Day 51 — Structured Claims and Evidence Verification

[English](notes.md) · [Türkçe](notes.tr.md) · [Code](claim_review.py)

Day 50 checked schema and reference membership. Today compare atomic claims against a fictional host-controlled fact registry. A permitted reference does not support every possible claim about it. Verify exact field membership, type and value. Examples: count=3 is supported; count=4 conflicts; count=3.0 has the wrong type. Predict ten outcomes, add a permitted document and test conflicting facts. This verifies simple structured equality, not arbitrary natural-language entailment or the truth of source records. No LLM, real documents or external tools.

## Run
```bash
python3 labs/51-structured-claims-and-evidence-verification/claim_review.py
```
