# Day 38 — RAG Cache TTL, Document Versions and Revocation

[English](notes.md) · [Türkçe](notes.tr.md) · [Python exercise](rag_cache_demo.py)

## Follow-up to Day 37
Authorization checks on cache hits are essential, but **staleness** also matters. A user may retain access while an indexed document changes. A cache should not keep returning an obsolete document after its revision is updated.

## Model
A toy cache stores `(user, document)` plus its **policy revision**, **document version**, **expiry timestamp (TTL)** and text. Each read authorizes the user's *current* tenant and groups **before** checking the cached entry. A hit requires the policy and document versions to match and `now < expires_at`.

The exercise verifies an ordinary hit, cross-tenant denial, updated document refresh, TTL expiry and revocation. Cached text is always treated as untrusted source data, never system instructions.

## Reproduce
~~~bash
python3 labs/38-rag-cache-ttl-document-versions-and-revocation/rag_cache_demo.py
~~~

## Practice
1. Why must a document-version change invalidate a cache entry even if the tenant stays the same?
2. Why should access be checked before returning a cached result?
3. What should happen if revocation arrives while an answer is already generating?
4. How do distributed caches, index replication and policy propagation complicate this simple design?
5. Why is TTL not a substitute for authorization?

## Limits
This is a single-process, in-memory exercise with fake time and fictional text. Real AI systems need enforcement on every tool and document fetch; this demo proves no production guarantees.
