# Gün 5 — MCP, Connector Güvenliği, Tool Discovery ve Yetki Sınırları

[English](notes.md) · [Türkçe](notes.tr.md)

Amaç: Day 4 agent izinlerini gerçek connector mimarisine bağlamak. MCP standardını tanımak, modelin tool isteği ile sunucunun yetki kararı arasındaki farkı ve tool-result prompt injection riskini öğrenmek.

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

Model tool ve argüman önerebilir; host bunları kontrol etmelidir. Üretilmiş JSON yetki değildir.

## 2. MCP in context

Model Context Protocol, AI host/client ile server arasındaki tool, resource ve prompt entegrasyonuna yönelik protokoldür. Demo gerçek bir MCP implementasyonu değildir.

## 3. Tool discovery and descriptions

Tool tanımı ve açıklaması dış connector'dan gelebilir; instruction gibi görünse bile application policy değildir.

## 4. Identity and delegated access

User, AI host ve connector farklı kimliklerle çalışabilir. Hangi kimliğin izinlerinin kullanıldığını kontrol et; confused deputy riskini azalt.

## 5. Scopes and least privilege

Read-only iş için geniş write permission verme. Yetkiyi user/project/resource bazında daralt.

## 6. Argument schemas

Tool adı, tip, uzunluk, ID, operation ve scope kontrollerini deterministic kodla yap.

## 7. Resource isolation

Tenant/proje yetkisi server tarafında kontrol edilmeden içerik modele dönmemeli.

## 8. Tool-result injection

Tool result içindeki emir cümlesi data olarak kalmalı; connector'dan geldi diye policy'ye dönüşmemeli.

## 9. OAuth and secrets

Tokenları prompt/log içine sokma; scoped credential, authorization flow ve revocation düşün.

## 10. Human approval

Dış sisteme yazma/silme gibi işlemlerde açık onay göster, execute sırasında yetkiyi tekrar doğrula.

## 11. Auditing and provenance

Actor, tool, scope, allow/deny, request ID ve sonucu logla; secret/içeriği gereksiz loglama.

## 12. Failure and retries

Timeout action gerçekleşmedi demek değildir. Side-effect için idempotency; belirsiz yetkide deny.

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
