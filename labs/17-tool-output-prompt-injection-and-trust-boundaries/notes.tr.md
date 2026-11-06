# Gün 17 — Araç Çıktısında Prompt Injection ve Güven Sınırları

[English](notes.md) · [Türkçe](notes.tr.md)

## Amaç
Bir yapay zekâ asistanının okuduğu web sayfası, belge veya araç çıktısının **veri** olduğunu, yetkili komut olmadığını öğrenmek. Dış kaynaklı metnin iş akışına müdahale etmesini çevrimdışı örnekle incelemek.

## Kavramlar
- **Prompt injection:** Düşük güvenilirlikteki metinle asistanın talimatlarını değiştirmeye çalışma.
- **Güven sınırı:** Kullanıcının/sistemin yetkili isteği ile üçüncü taraf içeriğin ayrıldığı nokta.
- Model "emin" görünse bile araç çalıştırma izni oluşmaz.
- Metin filtreleri tek başına tam çözüm değildir. Yetki sınırları, araç izinleri ve çıktı doğrulaması model dışında da uygulanmalıdır.

## Uygulama
```bash
python3 tool_output_boundary_demo.py
```
Bu kod **gerçek LLM içermez**. Kaynak metnini yalnızca veri olarak tutup önceden izin verilen işlemi korur. Dolayısıyla gerçek yapay zekâ saldırılarına karşı başarı oranı ölçmez.

## Görevler
1. Araç çıktısını hangi taraf kontrol ediyor?
2. Metin içindeki talimata uymak neden yetki ihlalidir?
3. Yeni bir saldırı dizesi ekle ve yetkili eylemin değişmediğini doğrula.
4. Gerçek LLM uygulaması için araç izinleri ve şema doğrulamasını öner.
5. Deney yapacak olsan saldırı başarı oranını nasıl ölçerdin?

## Güvenlik
Tamamen sentetik ve yerel örnek; hesap bilgisi veya dış sistem yok.
