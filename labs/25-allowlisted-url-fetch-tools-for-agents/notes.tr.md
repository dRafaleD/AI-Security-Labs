# Gün 25 — Ajanlar İçin İzin Listeli URL Getirme Araçları

[English](notes.md) · [Türkçe](notes.tr.md)

## Dersin amacı
Bu gün **Ajanlar İçin İzin Listeli URL Getirme Araçları** konusunu kontrollü, zararsız bir örnekte öğreniyoruz. Kavramları anlamak, hipotez kurmak ve gözlemi yorumdan ayırmak öncelikli.

## Temel bilgiler
1. Bir getirme aracı yalnızca ayrıştırılmış host'u izin listesinde olan https URL'lerini kabul etmelidir.
2. URL'yi alt dize aramak yerine ayrıştır; `https://good.test@evil.test/` adresinin host'u `evil.test`'tir.
3. Her yönlendirme hedefinde politikayı yeniden kontrol et; güvenilen bir host başka yere yönlendirebilir.

## Kavramsal ayrımlar
- İzin listesi ajanın nereye eriştiğini sınırlar; getirilen içeriği güvenilir yapmaz.
- Bir host adı çözümlense bile iç adresler ayrıca engellenmelidir.
- Getirilen metin veridir ve ajan için talimat olarak ele alınmamalıdır.

## Lab uygulaması
Önce `fetch_policy_demo.py` dosyasını incele. Komutları lab klasöründen çalıştır:

~~~bash
python3 fetch_policy_demo.py
~~~


## Görevler
1. Beş URL'den hangilerinin izinli olacağını tahmin et.
2. Demoyu çalıştırıp her ret nedenini not et.
3. Bir yönlendirme zinciri ekle ve her adımı kontrol et.
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
