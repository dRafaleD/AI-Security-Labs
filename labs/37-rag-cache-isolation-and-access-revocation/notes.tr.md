# Gün 37 — RAG Önbelleğinde Tenant İzolasyonu ve Yetki İptali

[English](notes.md) · [Türkçe](notes.tr.md) · [Python uygulaması](cache_acl_demo.py)

## 36. günden devam
RAG belgelerini sıralamadan önce erişim kontrolü yapmak yeterli değildir; **cache (önbellek)** eski veya başka kullanıcıya ait veriyi yanlışlıkla yeniden sunabilir.

**Cache key:** önbellekteki kaydı tanımlayan anahtar. **Revocation:** önceden verilmiş erişim hakkını geri alma. **Policy revision:** yetkiler değiştiğinde artırılan politika sürümü.

Üç hayalî belge ve iki tenant kullanıyoruz. Önbellek anahtarı `(kullanıcı, belge, politika sürümü)` içerir. Her okumada güncel yetki yeniden kontrol edilir. Alice'in okuyucu yetkisi kaldırılınca eski cache girdisi bulunsa bile sonuç verilmez.

## Çalıştır
```bash
python3 labs/37-rag-cache-isolation-and-access-revocation/cache_acl_demo.py
```

## Sorular
Cache anahtarı neden yalnızca sorgu metni olamaz? Yetki, cevap oluşturulurken iptal edilirse ne olmalı? Yetkili belgedeki komut benzeri metin neden güvenilmeyen veridir?

## Sınır
Bu yalnızca yerel ACL modelidir; gerçek LLM, tenant servisi veya hassas veri kullanılmaz.
