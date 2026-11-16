# Gün 39 — RAG Cache Bütünlüğü ve Güvenilmeyen İçerik

[English](notes.md) · [Türkçe](notes.tr.md) · [Python uygulaması](cache_integrity_demo.py)

## 38. günden devam
Önceki gün cache süresi, belge sürümü ve yetki iptalini kontrol ettik. Peki cache içindeki metin **sonradan değiştirilirse**? TTL ve sürüm doğru olsa bile yanlış veri gösterilebilir.

**Cache integrity:** önbellekteki baytların beklenen veriyle eşleşmesi. **Authoritative source:** uygulamanın güvenilir kabul ettiği asıl veri kaynağı. **SHA-256:** metnin değişip değişmediğini karşılaştırmak için kullanılan kriptografik özet.

Kod önce güncel kullanıcı/tenant yetkisini doğrular. Sonra cache TTL, politika sürümü, belge sürümü ve hash'i kontrol eder. Sadece cache metnini değiştirmek de, **metinle birlikte cache hash'ini değiştirmek de** asıl belgenin hash'iyle karşılaştırmada başarısız olur.

## Çalıştırma
~~~bash
python3 labs/39-rag-cache-integrity-and-untrusted-content/cache_integrity_demo.py
~~~

## Sorular
Sadece cache hash'ini doğrulamak neden yetersiz? Asıl belge kaynağı da değiştirilirse ne olur? Cache'de saklanan `IGNORE ALL PRIOR RULES` ifadesi neden uygulanacak komut değil, yalnızca veridir?

## Sınırlar
Gerçek RAG, LLM veya veritabanı kullanılmaz. Hash kontrolü bir kaynağın güvenilir veya doğru olduğunu tek başına garanti etmez.
