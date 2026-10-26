# Gün 19 — Araç Çağrılarında Nesne Düzeyinde Yetkilendirme

[English](notes.md) · [Türkçe](notes.tr.md)

## Dersin amacı
Bu gün **Araç Çağrılarında Nesne Düzeyinde Yetkilendirme** konusunu kontrollü, zararsız bir örnekte öğreniyoruz. Kavramları anlamak, hipotez kurmak ve gözlemi yorumdan ayırmak öncelikli.

## Temel bilgiler
1. Şema doğrulamasından geçen bir araç çağrısı, kullanıcının görmemesi gereken bir nesneye yine de başvurabilir.
2. Yetkiyi her zaman doğrulanmış oturum kullanıcısına göre ver; modelin veya prompt'un öne sürdüğü kimliğe ya da role göre değil.
3. Olmayan ve yasaklı nesne için aynı cevabı dön; böylece model hangi ID'lerin var olduğunu yoklayamaz.

## Kavramsal ayrımlar
- Şema doğrulaması "biçim doğru mu?" sorusunu, yetkilendirme "çağıran buna izinli mi?" sorusunu yanıtlar.
- System prompt'taki bir talimat modele yönelik bir öneridir, erişim kontrolü değildir.
- Hangi değerlerin oturumdan, hangilerinin model çıktısından geldiğini ayırt et.

## Lab uygulaması
Önce `authz_demo.py` dosyasını incele. Komutları lab klasöründen çalıştır:

~~~bash
python3 authz_demo.py
~~~


## Görevler
1. Demoyu çalıştırmadan önce yazdırılacak üç sonucu tahmin et.
2. Çalıştırıp hangi çağrının veri, hangisinin hata döndürdüğünü not et.
3. Oturum kullanıcısını `bob` yap ve sonuçların nasıl değiştiğini açıkla.
4. Modelin verdiği bir `owner` argümanının yok sayıldığını doğrulayan bir assertion ekle.
5. Nesnenin var olduğu ama başka bir kiracıya ait olduğu bir negatif senaryo yaz.
6. Aracı destekleyen bağımsız bir kontrol öner (ör. veritabanında satır düzeyi politika).

## Kısa sınav
1. Girdi nereden geliyor ve onu kim kontrol ediyor?
2. Doğrudan gözlenen ile çıkarım yapılan arasındaki fark nedir?
3. Hangi varsayımlar gerçek sistemde geçerli olmayabilir?
4. Hangi kanıt tek başına yetersiz kalır?
5. Bir otomatik test neyi kontrol etmeli?

## Etik ve sınırlamalar
Yalnızca izinli sistemlerde ve sentetik verilerle çalış. Bu örnek tam bir tespit veya koruma ürünü değildir.
