# AI-Security-Labs

[🇬🇧 English](#english) | [🇹🇷 Türkçe](#türkçe)

# English

A beginner-friendly, hands-on repository for learning both **practical AI usage** and **AI security**.

The goal is to understand how modern LLM applications are structured, where trust boundaries exist, how data flows through prompts/tools/context, and how to design safer AI-assisted systems.

## Labs

- [Day 1 — How LLM Applications Work: Models, Prompts, Context, Tokens and Trust Boundaries](labs/01-llm-applications-and-trust-boundaries/notes.md)
- [Day 2 — Prompt Injection, Indirect Prompt Injection and Instruction/Data Separation](labs/02-prompt-injection-and-instruction-data-separation/notes.md)
- [Day 3 — RAG Security, Retrieval Trust, Source Provenance and Data Isolation](labs/03-rag-security-provenance-and-isolation/notes.md)
- [Day 4 — Agent Security, Tool Permissions, Authorization and Human Confirmation](labs/04-agent-security-tool-permissions-and-confirmation/notes.md)
- [Day 5 — MCP, Connector Security, Tool Discovery and Permission Boundaries](labs/05-mcp-connectors-and-tool-trust/notes.md)
- [Day 6 — Untrusted Model Output, Schema Validation and Safe Rendering](labs/06-untrusted-model-output-schema-and-safe-rendering/notes.md)
- [Day 7 — LLM Security Evaluations, Adversarial Test Cases and Regression Gates](labs/07-security-evaluations-and-regression-gates/notes.md)
- [Day 8 — Sensitive Data Exposure, Secret Minimization and Tool Output Boundaries](labs/08-secret-minimization-and-sensitive-tool-output/notes.md)

- [Day 9 — RAG Poisoning, Source Provenance and Regression Tests](labs/09-rag-poisoning-source-provenance-and-evaluation/notes.md)

- [Day 10 — Agent Approval Gates, Argument Validation and Replay Protection](labs/10-10-agent-approval-gates-and-replay-protection/notes.md)

- [Day 11 — LLM Output Validation and Prompt-Injection Regression Gates](labs/11-llm-output-validation-and-injection-regression/notes.md)

- [Day 12 — Tool Result Provenance, Citation Checks and Grounding](labs/12-tool-result-provenance-and-grounding/notes.md)

- [Day 13 — LLM Audit Logging, Redaction and Data Minimization](labs/13-llm-audit-logging-and-data-minimization/notes.md)

- [Day 14 — Agent Loop Controls, Tool Budgets and Fail-Closed Policies](labs/14-tool-call-budgets-and-agent-loop-controls/notes.md)

- [Day 15 — Prompt Injection Taint Tracking and Safe Tool Routing](labs/15-prompt-injection-taint-and-tool-routing/notes.md)

## Learning path

Future labs will gradually cover:

- LLM fundamentals and application architecture
- prompts, system/user/tool roles
- tokens, context windows and truncation
- hallucination and reliability boundaries
- prompt injection and indirect prompt injection
- insecure output handling
- secret and sensitive-data exposure
- RAG security
- embedding/vector-store considerations
- tool and agent security
- MCP and connector trust boundaries
- authorization for AI actions
- logging and monitoring
- AI supply-chain risks
- secure AI application design
- red-team and evaluation methodology

## Lab philosophy

Each day combines multiple related concepts, practical examples, a local lab, review questions, and a mini challenge.

The goal is not to memorize prompt tricks. It is to understand where data comes from, which component is trusted, what the model can and cannot guarantee, and where the application must enforce security.

## Safety and ethics

Use AI-security exercises only on systems, applications, prompts, models, or environments that you own or are explicitly authorized to test. Do not place real secrets or sensitive personal data into training labs.

# Türkçe

Hem **pratik yapay zeka kullanımı** hem de **AI güvenliği** öğrenmek için temelden başlayan uygulamalı bir repo.

Amaç modern LLM uygulamalarının nasıl kurulduğunu, trust boundary'lerin nerede oluştuğunu, prompt/tool/context arasındaki veri akışını ve daha güvenli AI destekli sistemlerin nasıl tasarlanacağını anlamaktır.

## Lab'ler

- [Gün 1 — LLM Uygulamaları Nasıl Çalışır: Model, Prompt, Context, Token ve Trust Boundary](labs/01-llm-applications-and-trust-boundaries/notes.tr.md)
- [Gün 2 — Prompt Injection, Indirect Prompt Injection ve Instruction/Data Ayrımı](labs/02-prompt-injection-and-instruction-data-separation/notes.tr.md)
- [Gün 3 — RAG Güvenliği, Retrieval Trust, Source Provenance ve Data Isolation](labs/03-rag-security-provenance-and-isolation/notes.tr.md)
- [Gün 4 — Agent Güvenliği, Tool Permission, Authorization ve Human Confirmation](labs/04-agent-security-tool-permissions-and-confirmation/notes.tr.md)
- [Gün 5 — MCP, Connector Güvenliği, Tool Discovery ve Yetki Sınırları](labs/05-mcp-connectors-and-tool-trust/notes.tr.md)
- [Gün 6 — Güvensiz Model Çıktıları, JSON Schema ve Güvenli Rendering](labs/06-untrusted-model-output-schema-and-safe-rendering/notes.tr.md)
- [Gün 7 — LLM Güvenlik Değerlendirmesi, Saldırgan Test Vakaları ve Regression Kontrolleri](labs/07-security-evaluations-and-regression-gates/notes.tr.md)
- [Gün 8 — Hassas Veri Sızıntısı, Secret Minimization ve Tool Çıktısı Sınırları](labs/08-secret-minimization-and-sensitive-tool-output/notes.tr.md)

- [Gün 9 — RAG Zehirlenmesi, Kaynak Kökeni ve Regresyon Testleri](labs/09-rag-poisoning-source-provenance-and-evaluation/notes.tr.md)

- [Gün 10 — Agent Onay Kapıları, Parametre Doğrulama ve Tekrar Oynatma Koruması](labs/10-10-agent-approval-gates-and-replay-protection/notes.tr.md)

- [Gün 11 — LLM Çıktı Doğrulama ve Prompt Injection Regresyon Kontrolleri](labs/11-llm-output-validation-and-injection-regression/notes.tr.md)

- [Gün 12 — Araç Çıktısı Kaynağı, Atıf Denetimi ve Dayanak Kontrolü](labs/12-tool-result-provenance-and-grounding/notes.tr.md)

- [Gün 13 — LLM Denetim Günlükleri, Maskeleme ve Veri Minimizasyonu](labs/13-llm-audit-logging-and-data-minimization/notes.tr.md)

- [Gün 14 — Agent Döngü Kontrolü, Araç Bütçeleri ve Kapalı-Hata İlkesi](labs/14-tool-call-budgets-and-agent-loop-controls/notes.tr.md)

- [Gün 15 — Prompt Injection Veri Kaynağı Takibi ve Güvenli Araç Yönlendirme](labs/15-prompt-injection-taint-and-tool-routing/notes.tr.md)

## Öğrenme yolu

İlerleyen lab'lerde:

- LLM temelleri ve application architecture
- prompt, system/user/tool rolleri
- token, context window ve truncation
- hallucination ve reliability sınırları
- prompt injection ve indirect prompt injection
- insecure output handling
- secret ve sensitive-data exposure
- RAG security
- embedding/vector-store riskleri
- tool ve agent security
- MCP ve connector trust boundary'leri
- AI action authorization
- logging ve monitoring
- AI supply-chain riskleri
- secure AI application design
- red-team ve evaluation methodology

konuları adım adım işlenecektir.

## Lab yaklaşımı

Her gün birbiriyle ilişkili birkaç kavram, pratik örnekler, local lab, tekrar soruları ve mini challenge içerir.

Amaç prompt hilesi ezberlemek değil; verinin nereden geldiğini, hangi component'in trusted olduğunu, modelin neyi garanti edemediğini ve security enforcement'ın uygulamanın hangi katmanında yapılması gerektiğini anlamaktır.

## Güvenlik ve etik

AI security çalışmalarını yalnızca sahibi olduğunuz veya test etmek için açık izin aldığınız sistem, uygulama, prompt, model ve ortamlarda gerçekleştirin. Training lab'lerine gerçek secret veya hassas kişisel veri koymayın.


## Latest lab

- **Day 17 — LLM Output Redaction and Secret Leakage**
- [English notes](labs/17-llm-output-redaction-and-secret-leakage/notes.md) · [Türkçe notlar](labs/17-llm-output-redaction-and-secret-leakage/notes.tr.md) · [Practical exercise](labs/17-llm-output-redaction-and-secret-leakage/redaction_demo.py)
