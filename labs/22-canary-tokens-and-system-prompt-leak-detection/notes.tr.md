# Gün 22 — Canary Token'lar ve System Prompt Sızıntısı Tespiti

[English](notes.md) · [Türkçe](notes.tr.md)

## Dersin amacı
Bu gün **Canary Token'lar ve System Prompt Sızıntısı Tespiti** konusunu kontrollü, zararsız bir örnekte öğreniyoruz. Kavramları anlamak, hipotez kurmak ve gözlemi yorumdan ayırmak öncelikli.

## Temel bilgiler
1. Canary, system prompt'a konan rastgele bir işaretçidir; model çıktısında görünürse prompt sızmış demektir.
2. Her oturum için yeni bir canary üret; böylece bir eşleşme hangi konuşmanın sızdırdığını gösterir.
3. Her çıktıyı kullanıcıya veya araca gitmeden önce tara; eşleşmede engelle ya da gizle.

## Kavramsal ayrımlar
- Canary yalnızca birebir sızıntıyı yakalar; prompt'un başka sözcüklerle anlatımı fark edilmez.
- System prompt'u gizli tutmaya güvenlik kontrolü olarak asla güvenme.
- Eşleşmeyi tam prompt'u değil oturum kimliğini yazarak logla; log'un kendisi sızıntı olmasın.

## Lab uygulaması
Önce `canary_demo.py` dosyasını incele. Komutları lab klasöründen çalıştır:

~~~bash
python3 canary_demo.py
~~~


## Görevler
1. Üç model çıktısından hangilerinin dedektörü tetikleyeceğini tahmin et.
2. Demoyu çalıştırıp her sonucu not et.
3. Prompt'u başka sözcüklerle anlatan bir çıktı ekle ve neden yakalanmadığını açıkla.
4. İki oturumun asla aynı canary'yi paylaşmadığını doğrulayan bir assertion ekle.
5. Saldırganın canary'yi basılmadan önce nasıl silebileceğini veya değiştirebileceğini anlat.
6. Bağımsız bir kontrol öner (hassas ifadeler için çıktı filtreleme gibi).

## Kısa sınav
1. Girdi nereden geliyor ve onu kim kontrol ediyor?
2. Doğrudan gözlenen ile çıkarım yapılan arasındaki fark nedir?
3. Hangi varsayımlar gerçek sistemde geçerli olmayabilir?
4. Hangi kanıt tek başına yetersiz kalır?
5. Bir otomatik test neyi kontrol etmeli?

## Etik ve sınırlamalar
Yalnızca izinli sistemlerde ve sentetik verilerle çalış. Bu örnek tam bir tespit veya koruma ürünü değildir.
