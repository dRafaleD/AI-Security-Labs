# Gün 34 — AI Ajanlarında Araç Çıktısı Bütçesi ve Güvenilmeyen Veri

[English](notes.md) · [Türkçe](notes.tr.md) · [Çevrimdışı Python lab](tool_output_guard_demo.py)

## 33. günün devamı
Önceki derste ajanın **kaç araç çağrısı yapabileceğini** ve bunların maliyetini sınırlandırdık. Ancak tek bir `search_index` çağrısı çok büyük metin döndürürse ne olacak? LLM bağlamı gereksiz içerikle dolabilir, maliyet artabilir ve arama sonuçlarındaki kötü niyetli talimatlar modele aktarılabilir.

Bu yüzden yalnızca **giden araç çağrısını** değil, **gelen araç çıktısını** da kontrol etmeliyiz.

## Güven sınırları
1. Araç adını gerçek uygulamada **güvenilir dispatcher** belirlemelidir. Araç çıktısında “ben yetkili aracım” yazması yeterli değildir.
2. Yanıtı modele vermeden önce **ham bayt boyutu** sınırlandırılmalıdır.
3. Geçersiz UTF-8 ve beklenmeyen biçimler uygun şekilde reddedilmelidir.
4. Kaynak metnini `untrusted_text` alanında, uygulamanın denetlediği metaveriyi `trusted_metadata` içinde saklıyoruz.
5. Audit için tüm içeriği loglamak yerine SHA-256 ve boyut gibi alanlar kullanılabilir.

**Kritik nokta:** Metne `untrusted_text` etiketi yapıştırmak onu sihirli biçimde güvenli yapmaz. Model, kötü amaçlı metinden yine etkilenebilir. Gerçek sistemde talimat/veri ayrımı, araç yetkileri, güvenli çıktılar ve bağımsız güvenlik politikası gerekir.

## Çalıştır
```bash
python3 tool_output_guard_demo.py
```
Program normal yanıtı, zararsız örnek kötü niyetli talimat metnini, aşırı büyük yanıtı, bozuk UTF-8 içeriği ve izinsiz araç adını sınar. Gelen metni **asla komut olarak çalıştırmaz**. Harici AI modeli veya internete erişim yoktur.

## Alıştırmalar
1. Çağrı sayısı sınırı ile yanıt boyutu sınırı neden farklı?
2. Çok büyük bir arama çıktısı modelin bağlamını nasıl etkiler?
3. Bir web sayfasındaki “önceki talimatları yok say” metni neden yetkili komut değildir?
4. Sadece tehlikeli kelime filtresiyle prompt injection neden tamamen engellenemez?
5. Maksimum bayt limitinin tam sınırında test yap.
6. Gerçek ajan sisteminde response timeout, decompression, şema doğrulama ve hassas veri koruması nereye yerleştirilir?

## Sınırlar
Bu çalışma **prompt injection korumasını kanıtlamaz**. Amaç güvenilmeyen araç çıktısının uygulamanın yetki ve bütçe mekanizmasından ayrı tutulmasını öğrenmektir.
