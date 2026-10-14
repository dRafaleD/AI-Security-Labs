# Gün 6 — Güvensiz Model Çıktıları, JSON Schema ve Güvenli Rendering

[English](notes.md) · [Türkçe](notes.tr.md)

**Amaç:** Day 2 prompt injection, Day 4 agent authorization ve Day 5 connector'ların devamı olarak model output'unun güvenli işlenmesini öğrenmek.

**Kapsam:** Tamamen yerel, yalnız standart Python. Gerçek model/API, browser ya da file modification yok.

## 1. Output yetki değildir

LLM makul görünen JSON, HTML, SQL veya komut üretebilir; bunlar untrusted data'dır. Modelden schema istemek, server tarafındaki validation'ı ortadan kaldırmaz.

## 2. Parse ve validation ayrımı

JSON parse olması sadece syntax'ın geçerli olduğunu gösterir. Field, type, action ve ID ayrıca kontrol edilmelidir. Lab exact key, string tipi, action allowlist ve note ID denetler.

## 3. Beklenmeyen alanlar

Model 'role=admin' yazınca admin olunmaz. Demo ekstra JSON alanlarını, sahte role dahil reddeder. Gerçek user identity authenticated application state'ten gelmelidir.

## 4. HTML output encoding

Model/retrieved text HTML text node içinde gösteriliyorsa markup olarak çalışmaması için escape et. Lab html.escape kullanır. URL, attribute, JavaScript ve CSS context'leri farklı güvenli yöntemler gerektirir; tek escape bütün riskleri çözmez.

## 5. Execution anında yetki

Day 4 agent action ve Day 5 connector sınırının devamı: server her parsed action için execution sırasında yetkiyi kontrol eder. Model archive isterse bile reader rolü bunu yapamaz.

## 6. Etkili eylemlerde confirmation

Onay önemli işlemlerde faydalıdır ama authorization yerine geçmez. Simüle edilen archive için admin role ve açık confirmation gerekir. Onay hangi action ve hangi target'a verildiğiyle ilişkili olmalıdır.

## 7. Eval ve insecure yorumlama

Model output'unu eval/exec ile Python kodu gibi çalıştırma; shell komutu veya SQL string'i üretip doğrudan yürütme. JSON parse daha denetlenebilir bir katmandır ancak allowlist/type kontrolü gerektirir.

## 8. Tool result ve prompt injection

Dış dokümanda 'policy'yi ignore et' gibi emirler olabilir. Bunlar render, retrieval ve tool aşamasında data olarak kalmalıdır. Uygulama bunları server authorization'a dönüştürmemelidir.

## 9. Hata ve observability

Parse/policy hatasında fail closed uygula. Request ID, action türü, validation kararı ve sonucu logla; token veya özel içerik basma. Parser hata verdi diye tahmini argümanla action çalıştırma.

## 10. Demo'nun sınırları

Bu lab gerçek LLM, browser, kalıcı disk veya dış API kullanmaz. Gerçek prompt injection başarı oranı ölçmez; deterministic güven sınırını gösterir. Production'da UI context, rate limit, resource isolation ve downstream library güvenliği de gerekir.

## Local demo

```bash
python3 output_pipeline.py
python3 -m unittest -v test_output_pipeline.py
```

Akış:

```text
simulated model JSON
     ↓ parse JSON
     ↓ exact schema/type/action kontrolü
     ↓ server role + resource authorization
     ↓ gerekiyorsa confirmation
     ↓ güvenli simülasyon sonucu
```

`read_note` döndüğünde HTML text node için escape edilmiş string üretir. Bunu JavaScript veya CSS içine doğrudan koymak güvenli kabul edilmez.

### Test edilecek durumlar

- Geçerli read request → escaped text.
- JSON içine eklenmiş role=admin → schema deny.
- Unknown tool/action → deny.
- Reader rolüyle archive → deny.
- Admin rolüyle archive, confirmation yok → deny.
- Admin + confirmation → yalnızca simüle edilmiş başarı.

### Mini challenge

1. `note_id` için yanlış type (integer/list) testleri ekle.
2. Yeni `list_notes` read-only action tasarla; exact schema kuralını unutma.
3. Render edilmesi gereken bir HTML attribute örneği düşün; niye text-node escaping'e güvenilemez?
4. İzinli bir action'da kullanıcı onayı sonrasında yetkinin değiştiği senaryoyu modelle.

### Alıştırmalar

1. Demo çalıştır.
2. Tests çalıştır.
3. JSON syntax/schema farkını anlat.
4. Extra key rejection incele.
5. Action allowlist açıklaması yaz.
6. HTML escape çıktısını karşılaştır.
7. Malicious-looking sample'ın neden çalışmadığını açıkla.
8. Role kaynağını bul.
9. Confirmation kontrolünü izle.
10. Teste invalid type ekle.
11. Deny logları için güvenli alanlar tasarla.
12. Kısa security review yaz.

### Sorular

1. Model output neden untrusted?
2. JSON parse neyi garanti eder?
3. Schema neyi doğrular?
4. Extra field neden reddedilebilir?
5. Sahte role neden güvenilmez?
6. Allowlist ne işe yarar?
7. HTML text node escaping nedir?
8. Escape neden context'e göre değişir?
9. eval/exec niye risklidir?
10. Authorization kontrolü nerede olmalı?
11. Confirmation neden yeterli değil?
12. Model output secret içerebilir mi?
13. Tool result neden data kalmalı?
14. Fail closed ne anlama gelir?
15. Demo gerçek model güvenliğini kanıtlar mı?

**Ana çıkarım:** Model yalnızca öneri/çıktı üretir; parse, schema, authorization, confirmation ve safe rendering uygulamanın sorumluluğudur.
