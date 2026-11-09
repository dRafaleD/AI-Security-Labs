# Gün 33 — Yapay Zekâ Ajanlarında Araç Kullanım Bütçesi ve Güvenli Ret

[English](notes.md) · [Türkçe](notes.tr.md) · [Çevrimdışı politika modeli](budget_guard_demo.py)

## Tek tek izinli işlemler bir araya gelince de risk doğabilir
32. günde bir ajanın planındaki **her adımın ayrı yetkilendirilmesini** incelemiştik. Ancak izinli olan bir araç binlerce kez çağrılırsa ne olur? Sürekli tekrarlanan arama işlemleri API kotasını, maliyet bütçesini veya sistem kaynaklarını tüketebilir.

Bu yüzden sadece `allowed_tools` listesi yetmez. **Kimin hangi kaynağa eriştiğini**, **kaç çağrı yapıldığını** ve **toplam maliyeti** uygulamanın denetlemesi gerekir. Bir LLM'nin “bütçem kaldı” demesine güvenilmez.

## Oyuncak güvenlik politikası
Örnekte gerçek servisler yerine uydurma `own-notes` kaynağı var:
- `search_index`: 2 bütçe birimi
- `read_document`: 1 bütçe birimi
- `export_data`: yasak
- Bir oturumda en fazla **2 kabul edilen çağrı**, toplam en fazla **3 birim maliyet**

Kontroller kabul kararından **önce** yapılır. Reddedilen istekler bu eğitim örneğinde kotadan düşmez; ancak gerçek sistemlerde reddedilen istekleri de hız sınırlamasına almak gerekebilir.

`BudgetGuard.authorize()` yalnızca karar üretir; gerçek arama, okuma veya dışarı veri aktarma **yapmaz**. Böylece ajan planı ile uygulamanın yetkilendirme katmanı ayrılmış olur.

## Çalıştır
```bash
python3 budget_guard_demo.py
```
Beklenen sıra: izinli arama, izinli okuma, üçüncü çağrının kota nedeniyle reddi, dışa aktarmanın politika nedeniyle reddi ve başka kullanıcı kaynağını okumanın reddi. `assert` kontrolleri kararları test eder.

## Görevler
1. Çağrı sayısı ile maliyet bütçesi neden farklıdır?
2. Binlerce kez reddedilen istek gelirse bu model neden yetersiz kalabilir?
3. Toplam bütçeyi 2'ye düşür: hangi işlem artık kabul edilmez?
4. Birden çok çalışan (worker) aynı anda sayaç güncelliyorsa neden **atomik kota ayırma** gerekir?
5. Retry, iptal veya çökme sonrası kotayı nasıl tutarlı saklarsın?
6. Gizli veri toplamadan hangi denetim (audit) alanlarını kaydedersin?

## Sınırlar
Burada LLM, internete erişim veya gerçek araç çağrısı yoktur. Gerçek uygulamada sayaçlar kullanıcı, tenant ve oturumla ilişkilendirilmeli; ortak kalıcı depoda tutulmalıdır. Ayrıca çıktı boyutu ve zaman aşımı gibi sınırlar gerekir.
