# Gün 23 — LLM Uç Noktalarında Hız Sınırlama ve Maliyet Kötüye Kullanımı

[English](notes.md) · [Türkçe](notes.tr.md)

## Dersin amacı
Bu gün **LLM Uç Noktalarında Hız Sınırlama ve Maliyet Kötüye Kullanımı** konusunu kontrollü, zararsız bir örnekte öğreniyoruz. Kavramları anlamak, hipotez kurmak ve gözlemi yorumdan ayırmak öncelikli.

## Temel bilgiler
1. Token bucket kısa patlamalara izin verir ama kullanıcı başına sürekli hızı sınırlar.
2. İstekleri yalnızca sayıya göre değil maliyete göre (ör. girdi boyutu) ücretlendir; tek bir dev prompt bütçeyi tüketmesin.
3. Yalnızca IP'ye değil kimliğe göre sınırla; sınırlayıcı durumu kullanılamazsa kapalı kal.

## Kavramsal ayrımlar
- Hız sınırları kötüye kullanımı ve faturayı azaltır; prompt injection veya veri sızıntısını durdurmaz.
- Çok sıkı bir sınır meşru kullanıcılara zarar verir; gözlenen kullanıma göre ayarla.
- İstekleri sessizce düşürmek yerine yeniden deneme ipucu içeren net bir 429 dön.

## Lab uygulaması
Önce `bucket_demo.py` dosyasını incele. Komutları lab klasöründen çalıştır:

~~~bash
python3 bucket_demo.py
~~~


## Görevler
1. Hızlı on isteğin kaçının kabul edileceğini tahmin et.
2. Demoyu çalıştırıp hangi isteklerin reddedildiğini not et.
3. Her isteğin maliyetini 5 yap ve etkisini anlat.
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
