# Day 44 — Strict Tool-Result Parsing and Duplicate-Key Defense

[English](notes.md) · [Türkçe](notes.tr.md) · [Python exercise](strict_result_demo.py)

## From Day 43
Day 43 used an application-controlled source ID and an allowlisted result schema. This lab closes another gap: JSON with **duplicate keys** can be interpreted differently by separate parsers, potentially changing the apparent meaning of a tool result.

## Parsing boundary
1. Check the user's source permission before interpreting the result.
2. Enforce a small raw UTF-8 byte limit.
3. Parse JSON while rejecting **all duplicate object keys**, including nested ones, and non-standard numbers such as `NaN`.
4. Accept exactly `kind=quote` and a bounded text string; reject unknown `role`, `source_id`, and tool-action fields.
5. Keep the accepted string **data only**, even if it contains an imitation system command.

The source ID comes from the host-controlled argument, never a value in the tool's JSON bytes. The 13 tests cover malformed or ambiguous input, cross-tenant denial and harmless quoted instruction text.

## Run
```bash
python3 labs/44-strict-tool-result-parsing-and-duplicate-key-defense/strict_result_demo.py
```

## Questions
Why do duplicate JSON members matter? Why validate bytes before normalizing text? Does schema validation guarantee content truthfulness? Where must tool dispatch authorization live? Can a quotation impersonating a system message acquire authority?

## Limits
No LLM, browser or real tool actions. This intentionally narrow parser does not implement full production input filtering, streaming or authentication.
