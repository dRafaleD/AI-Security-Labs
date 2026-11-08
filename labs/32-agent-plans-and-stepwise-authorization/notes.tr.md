# Gün 32 — Yapay Zekâ Ajanı Planı ve Her Adımda Yetkilendirme

[English](notes.md) · [Türkçe](notes.tr.md) · [Çevrimdışı uygulama](plan_guard_demo.py)

## Temel ayrım
Yapay zekâ ajanı birden fazla adımdan oluşan plan **önerebilir**; fakat bu plan kendiliğinden **yetki belgesi değildir**. Dosya okumaya verilen izin, dosyayı dışa aktarma, e-posta gönderme veya silme iznini kapsamaz. Her araç çağrısında ayrı politika kontrolü yapılmalıdır.

## Kontrolcü hangi alanlara bakar?
Her adım için **eylem**, **hedef kaynak**, **parametreler**, **işlemi başlatan kimlik** ve **onay durumu** ayrıştırılmalıdır. Kaynağın gerçek kimliği çözülmeden yetki kontrolü yapmak tehlikeli olabilir. "Ajan güvenilir" gibi tek bir bayrak, kaynak düzeyinde en az yetkinin yerini tutmaz.

## Önceki labla bağlantı
31. günde onayı belirli parametrelere ve son kullanma süresine bağladık. Bu defa aynı ilkeyi bir **işlem zincirine** uyguluyoruz: kullanıcı salt-okunur analize izin verebilir, ancak export için ayrıca onay gerekir. Bir adımın onayı sonraki adımlara otomatik aktarılmaz.

## Pratik
```bash
python3 plan_guard_demo.py
```

Üç sentetik istek bulunur: izinli **read**, izinsiz **export** ve kaynağı değiştirilmiş başka bir **read**. Program kararları raporlar; **hiçbir dosya üzerinde işlem yapmaz** ve LLM çalıştırmaz.

## Görevler
1. Hangi plan adımının reddedildiğini ve nedenini açıkla.
2. İkinci salt-okunur kaynağa açık izin ver ve sonucu karşılaştır.
3. Planı başta bir kez onaylamanın neden yeterli olmadığını anlat.
4. Onaydan sonra kaynak yolu değişirse nasıl davranılmalı?
5. Kimlik, kaynak ID, eylem, karar ve politika sürümü içeren denetim kaydı tasarla.

## Güvenlik ve sınırlamalar
Bu lab gerçek LLM dayanıklılık ölçümü değildir. Ağ, e-posta, dışa aktarma veya silme işlemi yapmaz.
