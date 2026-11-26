# Gün 50 — Çıktı Şeması Doğrulama ve Güvenli Çekimserlik

[English](notes.md) · [Türkçe](notes.tr.md) · [Code](output_gate.py)

49. günde veri minimizasyonu yaptık. Bugün hayalî özet çıktısını göstermeden önce doğruluyoruz: iki alan, sınırlı metin ve uygulamanın izinli referans listesinde bulunan kaynak. Tekrarlı JSON anahtarları, bilinmeyen referanslar ve fazladan işlem alanları reddedilir. Geçerli şema özetin doğru olduğunu kanıtlamaz. 12 senaryoyu çalıştır; eksik alan, uzun özet ve izinli kaynağa rağmen yanlış iddia örneği ekle. Son örneğin neden ayrıca anlamsal doğrulamaya ihtiyaç duyduğunu açıkla. Gerçek LLM veya belge kullanılmaz.

## Çalıştır
```bash
python3 labs/50-output-schema-validation-and-safe-abstention/output_gate.py
```
