# Gün 24 — Loglamadan Önce PII Tespiti ve Maskeleme

[English](notes.md) · [Türkçe](notes.tr.md)

## Dersin amacı
Bu gün **Loglamadan Önce PII Tespiti ve Maskeleme** konusunu kontrollü, zararsız bir örnekte öğreniyoruz. Kavramları anlamak, hipotez kurmak ve gözlemi yorumdan ayırmak öncelikli.

## Temel bilgiler
1. Kişisel veriyi log, trace ve analitiğe ulaşmadan maskele; çünkü bu depolar geniş kitlelerce okunabilir.
2. Desen tabanlı maskeleme e-posta ve kart benzeri numaralar gibi yapısal verileri yakalar, serbest metindeki isimleri değil.
3. Değeri saklamadan olayları ilişkilendirmen gerekiyorsa kısa ve geri döndürülemez bir parmak izi tut.

## Kavramsal ayrımlar
- Regex bir emniyet ağıdır, garanti değildir; sonradan maskelemek yerine ne logladığını tasarla.
- Yanlış pozitifler (kart olmayan uzun sayılar) kaçan sızıntılardan daha ucuzdur.
- Yalnızca sentetik veriyle test et; fixture'lara gerçek kişisel veri koyma.

## Lab uygulaması
Önce `mask_demo.py` dosyasını incele. Komutları lab klasöründen çalıştır:

~~~bash
python3 mask_demo.py
~~~


## Görevler
1. Maskelenmiş log satırının nasıl görüneceğini tahmin et.
2. Demoyu çalıştırıp iki e-postanın parmak izlerini karşılaştır.
3. Bir telefon numarası deseni ekle ve sentetik bir numarayla test et.
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
