# Gün 12 — Araç Çıktısı Kaynağı, Atıf Denetimi ve Dayanak Kontrolü

[English](notes.md) | [Türkçe](notes.tr.md)

## Hedef ve kapsam

Bu gün araç çıktısı kaynağı, atıf denetimi ve dayanak kontrolü konusunu kendi bilgisayarında zararsız örneklerle öğreniyorsun. Amaç çıktıyı ezberlemek yerine güven sınırlarını ve çalışma ortamının sonuçlara etkisini anlamak.

## Temel çıkarımlar

1. Retrieval authorization precedes evidence use.
2. A citation must support the stated claim.
3. Substring checks in this example are not semantic truth verification.

## Uygulamalı çalışma

`source_check.py` dosyasını incele ve aşağıdaki komutları klasörden çalıştır:

```bash
python3 source_check.py
```

## Analiz görevleri

1. Başlangıç sonucunu kaydet ve beklediğin sonuçla karşılaştır.
2. Tek bir zararsız girdiyi değiştir ve tekrar dene.
3. Olumlu ve olumsuz testlerin beklenen davranışı gösterdiğini doğrula.
4. İki olası yanlış pozitif veya yanlış negatif nedeni yaz.
5. Bağımsız doğrulama için ikinci bir yöntem öner.
6. Sonuç, belirsizlik ve sonraki adımı raporla.

## Mini görev

Örneği otomatik bir regresyon testine dönüştür. Korunmasını istediğin güvenlik özelliğini bir assertion ile göster.

## Tekrar soruları

1. Buradaki güven sınırı nedir?
2. Hangi sonuç gözlem, hangisi yorum?
3. Hangi çevresel faktörler sonucu değiştirebilir?
4. Hata durumunda sistem ne yapmalıdır?
5. Tek bir bulgu neden kesin güvenlik kanıtı değildir?
6. Regresyon testi neyi garanti eder, neyi etmez?

## Güvenlik

Yalnızca yerel, sentetik veya açık izinli sistemlerde çalış. Demo çıktıları gerçek saldırı veya üretim güvenliği kanıtı değildir.
