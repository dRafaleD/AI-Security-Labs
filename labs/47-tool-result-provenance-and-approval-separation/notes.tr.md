# Gün 47 — Araç Sonucu Kaynağı ve Onay Ayrımı

[English](notes.md) · [Türkçe](notes.tr.md) · [Code](approval_boundary.py)

46. günde kota dönemini ve replay kontrolünü öğrendik. Bugün belgeyi okuma izni ile belgeden gelen metni birbirinden ayırıyoruz. Hayalî onay nesnesi kullanıcı, belge ve epoch değerine bağlıdır. Okunan metin kendisini onay olarak tanıtsa da yeni yetki oluşturmaz. Geçerli sonuç yalnızca READ_DATA_ONLY olur.

**Sorular:** Okuma izni neden yazma izni değildir? Belgeden gelen metin neden onay kaydı sayılmamalı? Epoch değişince eski onay ne olur?

Gerçek AI ajanı, dış API veya işlem çalıştırma yoktur. Onay nesnesi güvenilen yerel kontrol katmanını temsil eder; gerçek kimlik doğrulaması veya tek kullanımlık yetki sağlamaz.

## Çalıştır
```bash
python3 labs/47-tool-result-provenance-and-approval-separation/approval_boundary.py
```
