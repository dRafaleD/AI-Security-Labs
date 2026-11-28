# Day 52 — Claim Units and Evidence Normalization

[English](notes.md) · [Türkçe](notes.tr.md) · [Code](claim_units.py)

Day 51 checked structured claims against evidence. Today compare integer quantities after explicit unit conversion. The fictional source doc-a reports 2048 B, which supports 2 KiB but not 2 B. Unknown units, missing evidence and contradictory values are separate outcomes. Predict the ten cases and add a 1 MiB to bytes comparison. Explain why a verified number does not prove a free-text summary. The source dictionary is a trusted toy input, not an authenticated retrieval system. No LLM or external tools.

## Run
```bash
python3 labs/52-claim-units-and-evidence-normalization/claim_units.py
```
