# Gün 35 — Yapay Zekâ Ajanlarında Kaynak Atfı, Alıntı ve Yetki Kapsamı

[English](notes.md) · [Türkçe](notes.tr.md) · [Çevrimdışı uygulama](citation_guard_demo.py)

## Önceki günle bağlantı
34. günde araç (tool) çıktısının boyutunu sınırlamayı ve içindeki metni **güvenilmeyen veri** olarak tutmayı öğrendik. Bu sefer ajan o metni kaynak gösterirse ne olacağını inceleyeceğiz.

Bir yanıtın sonuna **doc-a** yazmak, o belgenin gerçekten getirildiğini veya yanıtı desteklediğini kanıtlamaz. Model olmayan belge numarası uydurabilir; hatta yanlışlıkla başka bir müşterinin (tenant) belgesine atıf yapabilir.

## Kontrol katmanları
1. **Kaynak ID'si:** Belge numarası model tarafından serbestçe uydurulmaz; güvenilir denetleyici tarafından yönetilir.
2. **Getirilmiş olma şartı:** Atıf yapılan ID, o işlemde gerçekten getirilen belgeler arasında olmalıdır.
3. **Tenant sınırı:** A takımının işlemi, B takımına ait kaynağı kullanamaz.
4. **Bütünlük:** Belgenin SHA-256 özeti önceden kayıtlı sürümle karşılaştırılır; farklıysa içerik değişmiş olabilir.
5. **Talimat/veri ayrımı:** Belgede SYSTEM: ignore rules gibi bir satır olsa bile bu **talimat değil, belge içeriğidir**.
6. **Anlamsal doğruluk:** Bu kontrollerden geçen bir atıf bile “iddia gerçekten o metinden çıkar mı?” sorusunu **tek başına cevaplamaz**.

**Önemli:** SHA-256 eşleşmesi dosyanın doğru, güvenilir veya doğru kişiye ait olduğunu kanıtlamaz. Yalnızca kayıtlı baytlarla karşılaştırma yapar.

## Uygulama
~~~bash
python3 citation_guard_demo.py
~~~

Kod; izinli kaynak, uydurma ID, başka tenant belgesi, değiştirilmiş içerik ve içine kurgu talimat yazılmış belge örneklerini inceler. Gerçek LLM, internet veya belge erişimi yoktur.

## Görevler
1. Kaynak ID'sini model uydurursa hangi risk oluşur?
2. **Integrity, provenance, authorization, grounding** kavramlarını ayır.
3. Kaynak içindeki bir baytı değiştirip hash kontrolünü gözlemle.
4. Gerçek bir kaynağın yanlış konu için gösterilmesi neden yanıltıcıdır?
5. Üretilen cümlenin kaynak tarafından gerçekten desteklendiğini nasıl incelersin?
6. Multi-tenant RAG'de iki müşterinin belgelerinin karışmasını hangi kontroller engeller?

## Kısıtlar
Bu bir güvenli RAG ürünü değil; belirlenimci Python örneğidir. Gerçekte backend güveni, yetkili kaynağın seçilmesi, sürüm takibi ve model yanıtının ayrıca doğrulanması gerekir.
