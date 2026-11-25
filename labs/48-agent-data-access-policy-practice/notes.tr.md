# Gün 48 — Uygulama Günü: AI Ajanı Veri Erişim Politikası

[English](notes.md) · [Türkçe](notes.tr.md) · [Code](access_matrix.py)

Hayalî AI asistanı için varsayılan olarak reddeden erişim matrisi oluşturuyoruz. Kullanıcı, belge ve onay bilgileri güvenilen uygulama katmanından gelir. Tenant, izinli işlem, belge sınıfı, sahiplik ve onay kontrol edilir. ALLOW_DATA_ONLY gerçek işlem başlatmaz.

| Örnek | Beklenen |
|---|---|
| Alice kendi dahili raporunu okur | ALLOW_DATA_ONLY |
| Alice kısıtlı belgeyi onaysız okur | NEEDS_APPROVAL |
| Bob Alice'in kısıtlı belgesini onayla ister | DENY_RESTRICTED |
| Alice başka tenant belgesini ister | DENY_TENANT |
| Alice silme ister | DENY_ACTION |
| Auditor özet ister | DENY_ROLE |

**Alıştırmalar:** 15 sonucu tahmin et. Beta için yeni belge ekle ve iki tenant ile dene. Yeni yasak işlem ekleyip reddi doğrula. Onayın neden tenant yetkisi yerine geçmediğini açıkla. Değişiklikten önce erişim matrisini kâğıda çiz.

Beklenen sonuç: 15/15 access-policy cases passed. Onay başka bir doğrulayıcıdan gelmiş varsayılır. Gerçek AI ajanı, ağ veya belge erişimi yoktur.

## Çalıştır
```bash
python3 labs/48-agent-data-access-policy-practice/access_matrix.py
```
