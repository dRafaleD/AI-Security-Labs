# Day 5 — MCP, Connector Security, Tool Discovery and Permission Boundaries

[English](notes.md) · [Türkçe](notes.tr.md)

Goal: extend Day 4 agent permissions to real connector architecture. Understand MCP, the difference between model-proposed tool calls and server-enforced permissions, and tool-result prompt injection.

**Prerequisites:** Days 1–4; Python 3.10+. **Scope:** harmless local simulation, no account connection, no secrets, no external model.

## Architecture

```text
User identity ──> AI host ──> model proposes tool call
                        │
                        ▼
                  validate tool + arguments
                        │
                        ▼
                check user/resource permissions
                        │
                        ▼
               connector / external service
                        │
                        ▼
               untrusted tool-result DATA
                        │
                        ▼
                model receives labeled context
```

## 1. Model-to-tool boundary

A model can suggest tool names and arguments, but the host application must validate both. Never treat generated JSON as permission.

## 2. MCP in context

Model Context Protocol is a way to connect AI hosts, clients and servers with resources, prompts and tools. This demo illustrates security principles, not wire protocol compliance.

## 3. Tool discovery and descriptions

Tool names and descriptions may come from connected services. Treat their text as potentially untrusted; never elevate it to app policy.

## 4. Identity and delegated access

A user, an AI host and a connector may have different identities. Determine whose permissions a call uses and prevent confused-deputy access.

## 5. Scopes and least privilege

Prefer narrow, per-user, per-resource scopes; a read-only document task should not receive a broad write token.

## 6. Argument schemas

Validate types, lengths, identifiers, allowlisted operations and target scope in deterministic code.

## 7. Resource isolation

Multi-tenant retrieval needs server-side project/tenant checks before returning content to the model.

## 8. Tool-result injection

A document or tool response may contain imperatives. It remains data, not policy, including when returned by a trusted connector.

## 9. OAuth and secrets

Keep credentials outside model prompts and logs; use provider-supported authorization flows, short-lived scoped tokens where available, and revocation.

## 10. Human approval

Important external writes require a clear preview and approval, plus an authorization recheck at execution.

## 11. Auditing and provenance

Record actor, tool, resource scope, decision, request ID and outcome; avoid leaking document bodies or tokens.

## 12. Failure and retries

Tool timeouts may occur after a side effect; use idempotency keys for state-changing workflows, and fail closed when authorization is uncertain.

## Local lab / Yerel uygulama

```bash
python3 connector_boundary_demo.py
```

The script / Script: one authorized read, one cross-project denial, one unknown-tool denial, and one missing-resource result. It also prints malicious-looking *sample text* to show that application authorization does not change. A Python dataclass is not an MCP server; the purpose is boundary reasoning.

## Threat-model worksheet

| Boundary | Input | Required control | Evidence |
| --- | --- | --- | --- |
| Model → host | Proposed tool name + JSON arguments | Allowlist, schema | Rejected unknown tool |
| Host → connector | User/project identity | Resource authorization | Cross-project denial |
| Connector → model | Retrieved content | Label provenance; treat as data | Instruction-like text ignored by policy code |
| Host → external write | State-changing request | Confirmation, recheck, idempotency | Documented decision |

## Mini challenges / Mini görevler

1. Add a separate user who can access only project beta. Check both allow and deny cases.
2. Add `create_document` as an intentionally state-changing tool: require authorization, input length limits and an explicit `confirmed` flag; test denial by default.
3. Add a tool-result string claiming it has admin authority. Explain why it must not change server-side policy.
4. Design how a connector token would be stored, scoped, rotated and revoked **without** placing any real token in this lab.

## Exercises / Alıştırmalar

1. Draw host, client, connector server and external resource.
2. Mark every trusted/untrusted boundary.
3. Explain tool description vs tool permission.
4. Test an authorized request and a cross-project denial.
5. Add argument type/length validation.
6. Differentiate read-only, write and destructive tool calls.
7. Add resource scope to the audit record.
8. Simulate a connector response containing instruction-like data.
9. Explain confused deputy with two identities.
10. Outline a safe approval/retry workflow.

## Questions / Sorular

1. What is MCP for? / MCP ne için kullanılır?
2. Does tool discovery grant access? / Tool discovery yetki verir mi?
3. Why is tool output untrusted? / Tool result neden untrusted?
4. Who must enforce tenant scope? / Tenant scope kim kontrol eder?
5. Why isn't model JSON authorization? / Model JSON'u neden yetki değil?
6. Why keep credentials outside context? / Secret neden context dışında?
7. What needs human confirmation? / Hangi action onay ister?
8. What makes retries dangerous? / Retry neden riskli?
9. What audit fields help investigations? / Hangi log alanları yararlı?
10. What does fail closed mean? / Fail closed nedir?

## Key takeaway / Ana çıkarım

**The model proposes; the application validates and authorizes; the connector performs only bounded operations.**
