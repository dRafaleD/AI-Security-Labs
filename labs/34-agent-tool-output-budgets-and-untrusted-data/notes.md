# Day 34 — Agent Tool Output Budgets and Untrusted Data

[English](notes.md) · [Türkçe](notes.tr.md) · [Offline Python guard](tool_output_guard_demo.py)

## From limiting calls to limiting responses
Day 33 applied **per-session call counts and cost budgets** to an AI agent. Those limits do not bound the size of a single tool response. A supposedly simple document search might return megabytes of data, excessive context, sensitive strings or instructions written by a third party.

The controller needs **response-side safeguards** in addition to action-side authorization. Tool text is **untrusted data**, even when it came through an approved tool. The fact that a retrieval tool is permitted says nothing about the authority of the content it retrieves.

## Separate metadata from content
The offline fixture receives a tool name from the *simulated trusted dispatcher*, plus raw bytes from the *untrusted tool response*.
1. Accept only known, read-only tool names.
2. Enforce a raw byte limit **before decoding or placing text into an LLM context**.
3. Require valid UTF-8 for the teaching example.
4. Keep controller-provided tool identity separate from `untrusted_text`. Content may mention system roles or orders but never becomes a policy instruction.
5. Compute a SHA-256 content digest for audit/correlation without logging the entire response.

The returned envelope has `trusted_metadata` and `untrusted_text` keys. **A key label does not itself create a secure trust boundary.** Actual deployment must use strict role separation, safely designed prompts, tool result rendering and output schemas; a model could still be influenced by malicious text.

## Run the fixture
```bash
python3 tool_output_guard_demo.py
```
It checks a normal response, a response containing a fictional “ignore previous instructions” line, an oversized response, invalid UTF-8 and an unapproved tool. The code never invokes an LLM, searches the web, exports data or executes embedded text.

## Investigate
1. Why is a request-call budget not a tool-output-size budget?
2. What could happen if a 10 MB search result is sent directly into model context?
3. Why is “ignore previous instructions” still *data* when it appears inside retrieved text?
4. Explain why looking for a handful of dangerous phrases cannot reliably stop prompt injection.
5. Change `MAX_TOOL_BYTES` and test the exact boundary value.
6. In production, where would you enforce decompression limits, response timeouts, schema checks, data loss prevention and authorized source provenance?

## Limits and safety
No prompt-injection immunity is claimed. This is a deterministic **preprocessing and accounting** exercise, not a live agent attack simulation. Trusted tool identity requires real dispatcher authentication in a deployed system.
