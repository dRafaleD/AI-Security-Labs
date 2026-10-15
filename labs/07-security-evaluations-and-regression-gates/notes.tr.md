# Gün 7 — LLM Güvenlik Değerlendirmesi, Saldırgan Test Vakaları ve Regression Kontrolleri

[🇬🇧 English](notes.md) | [🇹🇷 Türkçe](notes.tr.md)

Bu gün önceki labların üzerine inşa edilen, yalnızca yerel ve zararsız eğitim verisi kullanan uygulamalı bir çalışmadır. Kodun her varsayımını incele; çıktıları otomatik güvenlik kanıtı sayma.

## Öğrenme hedefleri

- Security invariants
- Adversarial fixtures
- Ground truth
- Deterministic enforcement
- Evaluation metrics
- Version control
- Side-effect checks
- Regression gates

## Veri akışı ve tehdit modeli

```text
controlled training input
        ↓
parser / evaluator / analyst
        ↓
security or evidence check
        ↓
observable result
        ↓
review assumptions and limits
```

## 1. Security invariants

Hangi tool eylemlerinin ve veri erişimlerinin kod tarafından reddedileceğini net tanımla.

**Görev:** Bu kontrolün hangi yanlış yorum veya güven sınırı ihlalini önlediğini bir örnekle açıkla.

## 2. Adversarial fixtures

Prompt injection, tenant sınırı, tool yanlış kullanımı ve geçersiz çıktı için etiketli vaka tasarla.

**Görev:** Bu kontrolün hangi yanlış yorum veya güven sınırı ihlalini önlediğini bir örnekle açıkla.

## 3. Ground truth

Testi çalıştırmadan beklenen izin/red sonuçlarını yaz.

**Görev:** Bu kontrolün hangi yanlış yorum veya güven sınırı ihlalini önlediğini bir örnekle açıkla.

## 4. Deterministic enforcement

Yetki ve şema doğrulamasını LLM kararına bırakma; kod testi olarak doğrula.

**Görev:** Bu kontrolün hangi yanlış yorum veya güven sınırı ihlalini önlediğini bir örnekle açıkla.

## 5. Evaluation metrics

Saldırı başarısını, FP/FN'yi ve birden fazla denemedeki oranları ayrı değerlendir.

**Görev:** Bu kontrolün hangi yanlış yorum veya güven sınırı ihlalini önlediğini bir örnekle açıkla.

## 6. Version control

Anlamlı kıyas için model, prompt, tool, policy, sıcaklık ve veri sürümünü kaydet.

**Görev:** Bu kontrolün hangi yanlış yorum veya güven sınırı ihlalini önlediğini bir örnekle açıkla.

## 7. Side-effect checks

Asistan metinde reddetse bile yasak tool çağrısı yapabilir; log ve yan etkileri test et.

**Görev:** Bu kontrolün hangi yanlış yorum veya güven sınırı ihlalini önlediğini bir örnekle açıkla.

## 8. Regression gates

Değişikliklerden sonra testleri tekrarla; sentetik test gerçek model güvenliğini kanıtlamaz.

**Görev:** Bu kontrolün hangi yanlış yorum veya güven sınırı ihlalini önlediğini bir örnekle açıkla.

## Uygulama

Yalnızca repo içindeki dosyaları kullan. Bu örnek üretim ortamına kurulacak güvenlik servisi değildir.

```bash
python3 security_eval.py
```

## Test matrisi

| Senaryo | Beklenen | Neden |
|---|---|---|
| Valid training input | Kabul / eşleşme | Baseline |
| Wrong owner or header | Ret / eşleşmeme | Scope / structure |
| Truncated or missing field | Kontrollü hata | Input validation |
| Unrelated benign sample | Yanlış alarm yok | False-positive awareness |

## Alıştırmalar

1. Örneği çalıştır ve çıktıyı kaydet.
2. İlk varsayımını not et.
3. Olumlu senaryoyu doğrula.
4. Bir negatif senaryo ekle.
5. İkinci negatif senaryo ekle.
6. Bir sınır değeri dene.
7. İlgili kontrolü kaynak kodunda bul.
8. Gözlem ve çıkarımı ayrı yaz.
9. Tek bir kontrolü çalışma kopyasında değiştir.
10. Bütün senaryoları tekrar test et.
11. Sonuçların sınırlamalarını yaz.
12. Bir sayfalık kısa analiz raporu hazırla.

## Tekrar soruları

1. Bu labda hangi güven sınırı var?
2. Hangi veri kullanıcı tarafından kontrol ediliyor?
3. Olumlu testin amacı ne?
4. Negatif testin amacı ne?
5. Çıktı neyi gerçekten kanıtlıyor?
6. Çıktı neyi kanıtlamıyor?
7. En kritik input hangisi?
8. Bir sınır değeri örneği ver.
9. Fail-closed davranış nedir?
10. Bu labı prod ortamına doğrudan almak neden riskli?
11. Bir false positive senaryosu düşün.
12. Bir false negative senaryosu düşün.
13. Log hangi alanları taşımalı?
14. Hangi kişisel veri gereksiz?
15. Sürüm bilgisi niçin kaydedilir?
16. Kontrol değişince hangi testler tekrar koşulmalı?

## Mini projeler

1. Bir yeni negatif test ve beklenen çıktı ekle; çalıştırıp belgele.
2. Bir güvenlik varsayımını çalışma kopyasında boz; hangi testin yakaladığını açıkla.
3. Kaynak, hash, araç sürümü, komut, gözlem ve sınırlamalardan oluşan kısa rapor yaz.

## Özet

Kendi aracının gerçek davranışını ölç; sentetik örneği aşırı genelleme. Güvenlik kararı, izin ve adli çıkarım bağımsız doğrulama gerektirir.
