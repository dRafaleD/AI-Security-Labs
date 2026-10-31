# Gün 27 — Ret ve Güvenli Başarısızlık Regresyon Testleri

[English](notes.md) · [Türkçe](notes.tr.md)

## Dersin amacı
Bu gün **Ret ve Güvenli Başarısızlık Regresyon Testleri** konusunu kontrollü, zararsız bir örnekte öğreniyoruz. Kavramları anlamak, hipotez kurmak ve gözlemi yorumdan ayırmak öncelikli.

## Temel bilgiler
1. Reddedilmesi ve yanıtlanması gereken prompt'lardan oluşan küçük bir tablo tut ve her değişiklikte çalıştır.
2. İki hata türünü de izle: kaçırılan retler ve zararsız isteklerin gereksiz reddi.
3. Bir kontrol kapalı başarısız olduğunda kullanıcı yığın izi veya kısmi çıktı değil, net bir güvenli mesaj görmelidir.

## Kavramsal ayrımlar
- Anahtar kelime filtresi bir temeldir ve başka sözcüklerle anlatım onu atlatır; test tablosu bu boşluğu gösterir.
- Seti geçmek bilinen bir regresyon olmadığı anlamına gelir, sistemin güvenli olduğu anlamına gelmez.
- Tabloda sentetik ve zararsız prompt'lar kullan.

## Lab uygulaması
Önce `refusal_tests_demo.py` dosyasını incele. Komutları lab klasöründen çalıştır:

~~~bash
python3 refusal_tests_demo.py
~~~


## Görevler
1. Anahtar kelime filtresinin hangi vakalarda yanılacağını tahmin et.
2. Demoyu çalıştırıp kaçan reti ve gereksiz reddi not et.
3. Bir başka paraphrase vakası ekle ve beklenen sayıları güncelle.
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
