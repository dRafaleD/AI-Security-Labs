# Gün 26 — Model ve Konfigürasyon Sabitleme, Drift Kontrolleri

[English](notes.md) · [Türkçe](notes.tr.md)

## Dersin amacı
Bu gün **Model ve Konfigürasyon Sabitleme, Drift Kontrolleri** konusunu kontrollü, zararsız bir örnekte öğreniyoruz. Kavramları anlamak, hipotez kurmak ve gözlemi yorumdan ayırmak öncelikli.

## Temel bilgiler
1. Model sürümünü ve güvenlikle ilgili ayarları sabitle, çalışan konfigürasyonu onaylı bir parmak izi ile karşılaştır.
2. Anahtar sırası ve boşluklar sonucu değiştirmesin diye konfigürasyonun kanonik halini hash'le.
3. Drift için alarm ver ve yeni parmak izini onaylamadan önce değerlendirme setini yeniden çalıştır.

## Kavramsal ayrımlar
- Eşleşen hash konfigürasyonun değişmediğini kanıtlar, güvenli olduğunu değil.
- `latest` gibi kayan takma adlar sabitlemeyi anlamsız kılar; tam sürümü sabitle.
- Onaylı parmak izi, kurcalanabilecek sistemin dışında tutulmalıdır.

## Lab uygulaması
Önce `drift_demo.py` dosyasını incele. Komutları lab klasöründen çalıştır:

~~~bash
python3 drift_demo.py
~~~


## Görevler
1. Üç konfigürasyondan hangilerinin drift olarak işaretleneceğini tahmin et.
2. Demoyu çalıştırıp parmak izlerini not et.
3. Onaylı konfigürasyonda anahtarların sırasını değiştir ve parmak izinin aynı kaldığını doğrula.
4. Bir güvenlik özelliği için assertion ekle.
5. Bir negatif senaryo ve bir yanlış pozitif ihtimali yaz.
6. Bağımsız bir doğrulama yöntemi öner.

## Kısa sınav
1. Girdi nereden geliyor ve onu kim kontrol ediyor?
2. Doğrudan gözlenen ile çıkarım yapılan arasındaki fark nedir?
3. Hangi varsayımlar gerçek sistemde geçerli olmayabilir?
4. Hangi kanıt tek başına yetersiz kalır?
5. Bir otomatik test neyi kontrol etmeli?

## Etik ve sınırlamalar
Yalnızca izinli sistemlerde ve sentetik verilerle çalış. Bu örnek tam bir tespit veya koruma ürünü değildir.
