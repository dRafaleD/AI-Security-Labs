# Gün 38 — RAG Cache TTL, Belge Sürümü ve Yetki İptali

[English](notes.md) · [Türkçe](notes.tr.md) · [Python uygulaması](rag_cache_demo.py)

## 37. günden devam
Önceki gün RAG önbelleğinin kullanıcılar arasında veri sızdırmaması ve yetki iptalinin dikkate alınması gerektiğini gördük. Bu gün ayrıca **belge sürümü** ve **TTL (time to live, saklama süresi)** kontrolü ekliyoruz.

Bir belgenin sürümü değişirse, izinler aynı kalsa bile cache'teki eski içerik yeniden kullanılmamalı. Süre dolarsa kayıt tekrar değerlendirilir. Kullanıcı yetkisi iptal edilirse **cache hit olsa bile erişim reddedilir**.

## Çalıştırma
~~~bash
python3 labs/38-rag-cache-ttl-document-versions-and-revocation/rag_cache_demo.py
~~~
Program sahte kullanıcılar, belgeler ve zaman değerleri kullanır; hiçbir gerçek LLM veya sunucuya bağlanmaz.

## Sorular
Belge sürümü niçin cache anahtarının geçerliliğini etkiler? TTL ile yetki kontrolü arasındaki fark nedir? Dağıtılmış cache ve geç ulaşan yetki iptali nasıl risk yaratabilir?

## Sınır
Yerel eğitim simülasyonudur. Prompt injection içeren belge metinleri her koşulda güvenilmeyen veri olarak değerlendirilmelidir.
