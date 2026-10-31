# Gün 28 — Araç Çıktısını Kısaltma ve Veri Olarak Sarmalama

[English](notes.md) · [Türkçe](notes.tr.md)

## Dersin amacı
Bu gün **Araç Çıktısını Kısaltma ve Veri Olarak Sarmalama** konusunu kontrollü, zararsız bir örnekte öğreniyoruz. Kavramları anlamak, hipotez kurmak ve gözlemi yorumdan ayırmak öncelikli.

## Temel bilgiler
1. Araç çıktısının boyutunu model bağlamına girmeden önce sınırla ve kısaltmayı açıkça işaretle.
2. Çıktıyı sınırlandırılmış bir veri bloğuna sar; model ve loglar onu talimatlardan ayırabilsin.
3. Veri içindeki kendi ayırıcını kaçır veya kaldır; içerik bloğu erken kapatamasın.

## Kavramsal ayrımlar
- Ayırıcılar yapı sağlar; modelin enjekte edilmiş metni izlemesini durdurmaz.
- Kısaltma önemli bir kısmı kesebilir; özgün uzunluğu logla.
- Kısaltılmış ve tam çıktıları sonraki mantıkta farklı ele al.

## Lab uygulaması
Önce `truncate_demo.py` dosyasını incele. Komutları lab klasöründen çalıştır:

~~~bash
python3 truncate_demo.py
~~~


## Görevler
1. Sarmalanmış çıktının uzunluğunu tahmin et.
2. Demoyu çalıştırıp enjekte edilen kapanış etiketinin etkisizleştiğini kontrol et.
3. Sınırı 20 karaktere indir ve sonucu anlat.
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
