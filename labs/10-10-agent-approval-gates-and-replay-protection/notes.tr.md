# Gün 10 — Agent Onay Kapıları, Parametre Doğrulama ve Tekrar Oynatma Koruması

[English](notes.md) · [Türkçe](notes.tr.md)

## Hedef
Agent Onay Kapıları, Parametre Doğrulama ve Tekrar Oynatma Koruması konusunu tamamen yerel ve zararsız örneklerle öğrenmek. Gözlemlenen bulguyu yorumdan ayırmak ve kesin olmayan sonuçları abartmamak.

## Temel kavramlar
1. **tool-call requests as untrusted proposals:** Kavramın amacını, güven sınırını, olası hatalarını ve hangi durumda kullanılacağını açıklayın.
2. **allowlisted operations:** Kavramın amacını, güven sınırını, olası hatalarını ve hangi durumda kullanılacağını açıklayın.
3. **typed argument validation:** Kavramın amacını, güven sınırını, olası hatalarını ve hangi durumda kullanılacağını açıklayın.
4. **server-side authorization:** Kavramın amacını, güven sınırını, olası hatalarını ve hangi durumda kullanılacağını açıklayın.
5. **explicit approval for writes:** Kavramın amacını, güven sınırını, olası hatalarını ve hangi durumda kullanılacağını açıklayın.
6. **idempotency keys and replay prevention:** Kavramın amacını, güven sınırını, olası hatalarını ve hangi durumda kullanılacağını açıklayın.

## Uygulama
Lab klasöründe `approval_demo.py` dosyasını inceleyin ve şu komutları sırasıyla uygulayın:

```bash
python3 approval_demo.py
```

**Beklenen sonuç:** First attempt denied without approval; next succeeds; identical request ID is rejected as replay.

## Analiz defteri
Kullandığınız araç sürümünü, komutu, girdiyi, gördüğünüz çıktıyı, beklenmeyen olayları ve olası açıklamaları kaydedin. Ölçülen veri ile çıkarımı ayrı başlıklar altında yazın.

## Uygulama görevleri
1. Orijinal örneği çalıştırıp çıktıyı kaydedin.
2. Zararsız bir girdiyi değiştirerek sonucu önceden tahmin edin.
3. Bir negatif test ekleyin ve gerçekten hangi kontrolün başarısız olduğunu belirleyin.
4. Başlangıç dosyasına dönüp regresyon testi yapın.
5. İki olası yanlış pozitif açıklaması üretin.
6. Sonucu doğrulayacak bağımsız bir kanıt kaynağı önerin.
7. Belirsizlikleri açıkça yazan kısa bir rapor hazırlayın.

## Tekrar soruları
1. tool-call requests as untrusted proposals nedir, ne işe yarar, neyi garanti etmez?
2. allowlisted operations nedir, ne işe yarar, neyi garanti etmez?
3. typed argument validation nedir, ne işe yarar, neyi garanti etmez?
4. server-side authorization nedir, ne işe yarar, neyi garanti etmez?
5. explicit approval for writes nedir, ne işe yarar, neyi garanti etmez?
6. idempotency keys and replay prevention nedir, ne işe yarar, neyi garanti etmez?
7. Sonucun güvenilirliğini nasıl artırırsınız?
8. Hangi kontrolü otomatik regresyon testine dönüştürürsünüz?

## Kapsam
Bu lab yalnızca izinli, sentetik veriler içindir. Tek bir bulguyu kesin saldırı kanıtı saymayın.
