# Gün 41 — Araç Onayı, Kaynak Sürümü ve TOCTOU

[English](notes.md) · [Türkçe](notes.tr.md) · [Python uygulaması](approval_version_demo.py)

## 40. günden devam
RAG belgesinin metni güvenilir bir **işlem onayı** değildir. Bugün ek bir sorun var: onay verildikten sonra kaynak değişebilir.

**TOCTOU (Time-of-check / Time-of-use):** kontrol zamanı ile kullanım zamanı arasındaki değişiklik riski. **Resource version:** hedef verinin sürüm numarası. **Approval binding:** onayın kullanıcıya, tenant'a, eyleme ve kaynağa bağlanması.

Hayalî uygulama her çağrıda güncel sürümü, onayın süresini ve daha önce kullanılıp kullanılmadığını kontrol ediyor. Eski sürüme ait onay reddediliyor. Yazma yeteneği modelde **hiç yok**; onay var diye yazma yapılmıyor.

## Çalıştır
~~~bash
python3 labs/41-tool-approval-resource-version-and-toctou/approval_version_demo.py
~~~

## Sorular
Onay ile eylem arasında kaynak değişirse ne olur? Aynı onayı iki worker kullanırsa hangi yarış oluşabilir? Gerçek sistemde kontroller neden atomik uygulanmalı?

## Sınır
Gerçek agent veya araç çağrısı yoktur. Program sadece yetkilendirme kararlarını simüle eder.
