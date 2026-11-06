# Gün 30 — Ajan Hafızası Yazma Politikası ve Zehirleme Kontrolleri

[English](notes.md) · [Türkçe](notes.tr.md)

## Dersin amacı
Bu gün **Ajan Hafızası Yazma Politikası ve Zehirleme Kontrolleri** konusunu kontrollü, zararsız bir örnekte öğreniyoruz. Kavramları anlamak, hipotez kurmak ve gözlemi yorumdan ayırmak öncelikli.

## Temel bilgiler
1. Kalıcı ajan hafızası gelecekteki her konuşmanın girdisidir; kötü bir yazma, özgün sohbet bittikten çok sonra da etkisini sürdürür.
2. Yalnızca kullanıcının onayladığı gerçeklere yazmaya izin ver ve ajana talimat gibi okunan metni reddet.
3. Şüpheli bir kayıt izlenip silinebilsin diye her hafıza kaydının kaynağını ve zamanını sakla.

## Kavramsal ayrımlar
- Talimat benzeri metin filtresi bir temeldir; başka sözcüklerle anlatım geçebilir.
- Araçlardan veya web sayfalarından alınan içerik asla kullanıcı onaylı gerçek değildir.
- Kullanıcıların ajanın hatırladıklarını görmesine ve silmesine izin ver.

## Lab uygulaması
Önce `memory_policy_demo.py` dosyasını incele. Komutları lab klasöründen çalıştır:

~~~bash
python3 memory_policy_demo.py
~~~


## Görevler
1. Hangi hafıza yazmalarının kabul edileceğini tahmin et.
2. Demoyu çalıştırıp her ret nedenini not et.
3. Başka sözcüklerle yazılmış bir talimat ekle ve filtrenin neden kaçırdığını anlat.
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
