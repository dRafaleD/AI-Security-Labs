# Gün 31 — Araç Onayı Süresi ve Parametre Bağlama

[English](notes.md) · [Türkçe](notes.tr.md) · [Uygulama](approval_demo.py)

## Öğrenme amacı

Zararsız yerel veriyle **Araç Onayı Süresi ve Parametre Bağlama** konusunun güven sınırlarını ve kanıt değerlendirmesini öğren.

## Temel kavramlar

1. İnsan onayı belirli işlem, parametre ve geçerlilik süresine bağlanmalıdır; hassas işlem için genel bir 'evet' yeterli değildir.

2. Onay tekrar oynatılmamalı, süre dolunca veya kullanıldıktan sonra geçersiz olmalıdır. Parametre değişirse yeniden yetkilendirme gerekir.

3. Yetki kontrolü modelin dışında uygulanır; bu örnekte gerçek model ya da araç çağrısı yoktur.

## Güvenli pratik

Önce kaynak kodunu oku ve sonucu tahmin et:

```bash
python approval_demo.py
```

Çıktı sentetiktir; gerçek sisteme komut gönderilmez.

## Görevler

1. Girdi verisini ve güvenilmeyen alanları belirle.
2. Bir negatif ya da sınır örneği ekleyip test et.
3. Gözlem ve yorum farkını açıkla.
4. Gerçek ortamda hangi doğrulamaların gerektiğini yaz.

## Kontrol soruları

- Tek gösterge yeterli mi?
- Yanlış pozitif veya eksik kayıt nasıl oluşabilir?
- Sonucu tekrar üretmek için hangi girdileri saklamalısın?

## Güvenlik ve sınırlamalar

Bu çalışma gerçek malware, bulut hesabı, sistem müdahalesi veya dış ağ gerektirmez. Modelin basitliği gerçek platformla birebir eşitlik iddiası taşımaz.
