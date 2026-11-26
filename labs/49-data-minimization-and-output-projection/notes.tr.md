# Gün 49 — Veri Minimizasyonu ve Çıktı Alanı Kontrolü

[English](notes.md) · [Türkçe](notes.tr.md) · [Code](projection_demo.py)

48. günde belgenin okunmasına kimin yetkili olduğunu değerlendirdik. Bugün güvenilen uygulamadan hangi alanların çıkabileceğini sınırlandırıyoruz. Çıktı role özel izin listesinden oluşturulur. İzinli ve izinsiz alan birlikte istenirse hiçbir alan verilmez.

**Örnekler:** reader title isteyebilir; internal_id isteyemez. Auditor internal_id isteyebilir. title ile private_note birlikte istenirse tamamı reddedilir. On bir senaryoda hem karar hem çıktı anahtarları kontrol edilir.

**Alıştırma:** yalnızca title gören public rolü ekle; boş listeyi ve eksik alanı test et. İzinli summary içinde bulunan hassas metnin neden yalnızca alan kontrolüyle bulunamayacağını açıkla. Gerçek kimlik, hassas veri veya AI aracı kullanılmaz.

## Çalıştır
```bash
python3 labs/49-data-minimization-and-output-projection/projection_demo.py
```
