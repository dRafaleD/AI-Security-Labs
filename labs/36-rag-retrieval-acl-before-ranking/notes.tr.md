# Gün 36 — RAG'de Sıralamadan Önce Erişim Kontrolü

[English](notes.md) · [Türkçe](notes.tr.md) · [Python uygulaması](rag_acl_demo.py)

## 35. günden devam
35. gün, alıntının hangi kaynaktan geldiğini ve kaynağa erişim kapsamını kontrol ediyordu. Bu gün daha temel bir soruyu ele alıyoruz: **LLM'e sunulmadan önce hangi belgeler seçilebilir?**

**RAG:** modelin yanıt üretirken belgelerden bilgi çekmesi.
**ACL:** kullanıcı veya grubun erişebildiği kaynaklar.
**Tenant:** birbirinden ayrılmış müşteri/çalışma alanı.
**Top-k:** en yüksek puanlı k sonuç.
**Fail closed:** yetki kanıtlanamıyorsa erişimi reddet.

## Güvenli sıra
1. Kullanıcının kimliği ve grupları uygulama katmanında doğrulanır.
2. Belgeler önce **tenant ve grup yetkisine göre filtrelenir**.
3. Yalnızca izinli belgeler puanlarına göre sıralanır.
4. İlgili belgeler, **güvenilmeyen veri** olarak modele verilir.
5. Kaynak kimliği ve iddiayla uyumu ayrıca kontrol edilir.

Kod, dört hayalî belgeyi kullanır. Biri başka tenant'a, biri yönetici grubuna aittir. Birinde `IGNORE PREVIOUS INSTRUCTIONS` metni vardır; bu sadece belgedeki yazıdır, **uygulanacak talimat değildir**.

Önce tüm belgeleri sıralayıp sonra filtrelemek, en yüksek puanlı sonuç yetkisizse geçerli belgeyi atlayabilir. Böylece bu örnekte bir **geri getirme (recall) sorunu** oluşur.

## Çalıştırma
~~~bash
python3 labs/36-rag-retrieval-acl-before-ranking/rag_acl_demo.py
~~~

## Sorular
1. Kullanıcı grubunu neden doğrudan LLM cevabından almıyoruz?
2. Yetki iptal edilirse önbellek ne yapmalı?
3. Bir belgeye erişebilmek, o belgenin yanıtı doğruladığı anlamına gelir mi?
4. Belgedeki talimat benzeri metin neden çalıştırılmamalı?
5. Gerçek sistemde yetki hem arama hem belge indirme sırasında neden kontrol edilmeli?

## Sınırlar
Tamamen yerel, uydurma metinlerden oluşan bir uygulamadır; gerçek LLM, API veya gizli veri kullanılmaz.
