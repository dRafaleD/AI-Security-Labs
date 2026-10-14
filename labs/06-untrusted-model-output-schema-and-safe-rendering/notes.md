# Day 6 — Untrusted Model Output, Schema Validation and Safe Rendering

[English](notes.md) · [Türkçe](notes.tr.md)

**Goal:** continue Days 2, 4 and 5 by learning how to handle untrusted model outputs safely.

**Scope:** Python standard library only; no model/API, browser or filesystem modification.

## 1. Output is not authority

An LLM can produce plausible JSON, HTML, SQL or text, but its output remains untrusted. Even when the model was prompted to use a schema, the application must enforce that schema independently.

## 2. Parsing versus validation

JSON parsing only proves syntax. It does not prove that object fields, types or operations are allowed. This lab validates exact keys, string types, an action allowlist and note IDs before any simulated execution.

## 3. Unexpected fields

A model-generated role, owner or approval flag is not a trusted identity source. The demo rejects extra JSON keys, including a forged role field. True user identity must come from authenticated application state.

## 4. HTML output encoding

If model-generated or retrieved text is placed inside an HTML text node, escape HTML special characters to prevent it from becoming markup. This lab uses html.escape. Escaping depends on context: URL, HTML attribute, JavaScript and CSS need different safe APIs and policies.

## 5. Authorization at execution

In Day 4 the agent requested tools; in Day 5 connectors returned data. Here the server checks permission for each parsed action at execution time. A read role cannot archive even if the model proposes it.

## 6. Confirmation for impactful actions

A user approving an exact action is useful but not an authorization bypass. The simulated archive operation requires admin role and explicit confirmation. Confirmation must be bound to a specific action and target.

## 7. Insecure deserialization and dynamic evaluation

Never evaluate model text as Python code or use eval/exec, shell concatenation, or dynamic SQL. Parsing structured JSON is safer but still requires allowlists and type checks. Do not mistake natural-language instructions for executable policies.

## 8. Tool outputs and prompt injection

External retrieved material can contain imperative strings such as 'ignore the developer policy'. Those strings must remain data throughout rendering, retrieval and tool calls. The pipeline must resist promotion of such text into authorization.

## 9. Validation failure and observability

Fail closed on parse or policy errors. Log request ID, action category, validation result, permission decision and outcome while avoiding raw tokens and private text. An error should not silently fall back to executing guessed arguments.

## 10. Limits of the demo

There is no real LLM, browser, persistent storage or external API in this lab. It demonstrates boundaries deterministically, not empirical prompt-injection success rates. Real systems also require UI context validation, rate limits, resource isolation and safe downstream libraries.

## Local demo

```bash
python3 output_pipeline.py
python3 -m unittest -v test_output_pipeline.py
```

Pipeline:

```text
simulated model JSON
     ↓ JSON parsing
     ↓ exact schema/type/action validation
     ↓ trusted server-side role + resource authorization
     ↓ confirmation if necessary
     ↓ bounded simulated result
```

A `read_note` returns escaped text suitable for an HTML text node. This does not mean the same escaped output is safe for arbitrary JavaScript, CSS or URL contexts.

### Test expectations

- Valid read → escaped text.
- Extra forged `role=admin` field → schema denial.
- Unknown action → denial.
- Reader archive → denied.
- Admin archive without confirmation → denied.
- Admin archive with confirmation → simulated success, no persistent side effect.

### Mini challenges

1. Add wrong-type tests for note IDs (integer/list).
2. Design a new read-only `list_notes` action with an exact schema.
3. Explain why HTML text-node encoding alone cannot protect a JavaScript or CSS context.
4. Model an authorization change between preview and confirmation; require an execution-time recheck.

### Exercises

1. Run the demo.
2. Run unit tests.
3. Compare JSON syntax vs schema.
4. Inspect extra-key rejection.
5. Explain the allowlist.
6. Compare escaped and original HTML text.
7. Explain why an instruction-looking string does not execute.
8. Locate trusted role input.
9. Trace confirmation logic.
10. Add an invalid-type test.
11. Design safe audit fields.
12. Write a short code review.

### Review questions

1. Why is model output untrusted?
2. What does JSON parsing prove?
3. What does schema validation add?
4. Why reject extra fields?
5. Why not trust model-generated roles?
6. What does an action allowlist enforce?
7. What is HTML text-node escaping?
8. Why is encoding context-specific?
9. Why avoid eval/exec?
10. Where should authorization happen?
11. Why doesn't confirmation replace permission?
12. Can model output leak secrets?
13. Why must tool results remain data?
14. What is fail closed?
15. Does this lab prove any real model is secure?

**Takeaway:** The model proposes content; deterministic application code enforces schema, permissions, confirmation and context-safe presentation.
