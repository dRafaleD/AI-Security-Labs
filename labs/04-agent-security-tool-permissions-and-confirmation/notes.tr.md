# Gün 4 — Agent Güvenliği, Tool Permission, Authorization ve Human Confirmation

[🇬🇧 English](notes.md) | [🇹🇷 Türkçe](notes.tr.md)

## Amaç

AI agent'ın yalnızca text üretmek yerine action alabilmesiyle security riskinin neden arttığını anlamak.

Bu gün:

- agent vs chatbot,
- tool capability,
- least privilege,
- authentication vs authorization,
- argument validation,
- confirmation gate,
- read/write/destructive action,
- tool output trust,
- confused deputy,
- audit logging,
- deterministic enforcement

konularını birlikte işler.

Ana kural:

> Model action önerebilir; application bu action'ın izinli olup olmadığına karar verir.

## 1. Chatbot vs agent

~~~text
chatbot:
user -> model -> text

agent:
user -> model -> tool request -> policy -> execution
~~~

Agent gerçek side effect oluşturabildiği için risk artar.

## 2. Capability

Tool'un ne yapabildiği önemlidir:

- read,
- create,
- send,
- delete,
- publish,
- payment,
- permission change.

Hepsi aynı riskte değildir.

## 3. Least privilege

~~~text
task
  ↓
minimum tool
  ↓
minimum scope
  ↓
minimum permission
  ↓
minimum duration
~~~

Default admin vermek yerine ihtiyaca göre permission ver.

## 4. Authentication vs authorization

Authentication: user kim?

Authorization: bu tool action'ı yapabilir mi?

Conversation text'ten role tahmin edilmemelidir.

Server-side identity/policy kullanılmalıdır.

## 5. Tool pipeline

~~~text
model request
   ↓
tool valid mi?
   ↓
user authorized mı?
   ↓
arguments valid mi?
   ↓
scope allowed mı?
   ↓
confirmation gerekli mi?
   ↓
execute
   ↓
log
~~~

## 6. Argument validation

Model-generated argument doğrudan sensitive API'ye verilmemeli.

Kontrol et:

- field,
- type,
- length,
- enum,
- resource ID,
- scope.

## 7. Allowlisted tool

Narrow tool tercih et:

~~~text
read_note
create_note
~~~

yerine arbitrary shell/sql/admin tool expose etme.

## 8. Action impact

Read daha düşük riskli olabilir ama sensitive data leak edebilir.

Write state değiştirir.

Destructive action delete/revoke/overwrite/publish gibi daha yüksek risk taşır.

## 9. Human confirmation

~~~text
model action önerir
   ↓
app exact action gösterir
   ↓
user confirm
   ↓
server authorization tekrar check
   ↓
execute
~~~

## 10. Confirmation authorization değildir

User “yes” dedi diye unauthorized action allowed olmaz.

Önce authorization, sonra gerekiyorsa confirmation.

## 11. Confused deputy

Low-privilege user, high-privilege component'i kendi adına sensitive action yapmaya yönlendirebilir.

Defense: tool boundary'de deterministic authorization.

## 12. Model confidence permission değildir

Modelin “eminim authorized” demesi security evidence değildir.

Permission trusted application state'ten gelir.

## 13. Tool output da untrusted olabilir

Webpage/email/document döndüren tool'lar instruction-like text getirebilir.

Tool output data olarak kalmalıdır.

Day 2-3 ile bağlantılıdır.

## 14. Local demo

~~~bash
python3 agent_tool_security_demo.py
~~~

External model/API yok.

Tool'lar:

- read_note,
- create_note,
- delete_note.

Role policy + validation + confirmation gösterilir.

## 15. Gözlem

Student read yapabilir.

Student delete yapamaz.

Admin delete authorization geçse bile confirmation ister.

Bu pattern'i öğren.

## 16. Tool schema

Narrow schema:

~~~json
{"tool":"read_note","arguments":{"name":"welcome"}}
~~~

geniş arbitrary command tool'dan daha güvenlidir.

## 17. Scope

Tool permission resource scope ile sınırlandırılmalı.

Örneğin GitHub tool sadece tek repo + issue create yetkisi alabilir.

## 18. Secret

API token model context'e verilmemeli.

Tool credential'ı internally kullanabilir.

## 19. Audit

Log:

- user,
- tool,
- validated args,
- authorization,
- confirmation,
- result,
- timestamp,
- request ID.

Secret loglama.

## 20. Fail closed

Policy kararsızsa:

~~~text
uncertain -> deny / review
~~~

default privileged execution yapma.

## 21. Retry

Agent aynı action'ı retry edebilir.

State-changing action için:

- idempotency key,
- duplicate detection,
- request ID

düşün.

## 22. Partial failure

Tool timeout olabilir ama action gerçekleşmiş olabilir.

~~~text
no response != no side effect
~~~

Retry öncesi state kontrolü gerekir.

## 23. Mini challenge — email

draft_email / send_email tasarla.

Send:

- authorized,
- recipient validated,
- exact content confirmed,
- credential hidden,
- request ID

olmalı.

## 24. Mini challenge — GitHub

Tek repo için issue-create tool tasarla.

Allowed repo/action/schema/auth/logging belirle.

## 25. Mini challenge — archive

archive_note ekle.

Read/write/destructive sınıfını seç ve policy + confirmation tasarla.

## 26. Checklist

~~~text
1. Tool'lar ne?
2. Read/write/destructive hangisi?
3. Kim kullanabilir?
4. Args validate ediliyor mu?
5. Scope dar mı?
6. Secret modelden gizli mi?
7. Confirmation var mı?
8. Execute anında auth tekrar check mi?
9. Retry safe mi?
10. Tool output data mı?
11. Audit var mı?
12. Fail closed mu?
~~~

## Alıştırmalar

1. Demo çalıştır.
2. Student delete neden denied açıkla.
3. Admin delete neden confirmation ister açıkla.
4. Read-only tool ekle.
5. Length validation ekle.
6. Archive tool tasarla.
7. Tool'ları impact'e göre sınıflandır.
8. Email flow tasarla.
9. GitHub flow tasarla.
10. Request ID ekle.
11. Retry riskini açıkla.
12. Confused deputy'yi kendi cümlenle açıkla.

## Sorular

1. Agent neden chatbot'tan riskli?
2. Least privilege nedir?
3. Authentication vs authorization?
4. Args neden validate edilir?
5. Narrow tool neden iyi?
6. Confirmation neden auth yerine geçmez?
7. Confused deputy nedir?
8. Credential neden model context dışında kalmalı?
9. Retry neden riskli?
10. Tool output neden untrusted olabilir?
11. Ne loglanmalı?
12. Fail closed ne demek?

## Ana çıkarım

~~~text
model proposes
   ↓
application validates
   ↓
application authorizes
   ↓
confirmation
   ↓
bounded tool
   ↓
audit
~~~

Agent security, model niyetine güvenmekten çok capability kontrolüdür.
