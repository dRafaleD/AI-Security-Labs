# Day 37 — RAG Cache Isolation and Access Revocation

[English](notes.md) · [Türkçe](notes.tr.md) · [Python exercise](cache_acl_demo.py)

## After Day 36
Filtering RAG documents **before ranking** is necessary, but a retrieval cache can bypass that boundary if a cached result is reused across tenants, users or outdated permissions.

**Cache key:** an identifier for stored retrieval data. **Revocation:** removal of access rights. **Policy revision:** an application-managed version that changes when permissions change.

## Model
Three fictional documents belong to two tenants. `fetch()` verifies the current application's authorization **before every cache hit**. Cache keys contain `(user, document ID, policy revision)`, rather than only the search term. Revoking Alice's `readers` group makes her previously cached document inaccessible; the old cache entry may remain but is never returned.

## Run
```bash
python3 labs/37-rag-cache-isolation-and-access-revocation/cache_acl_demo.py
```

## Exercises
1. Why can't a shared cache use just the query text as its key?
2. What happens if access changes while an LLM is generating?
3. What distinguishes cache invalidation from authorization at disclosure?
4. Why are text snippets still untrusted even if access checks pass?

## Limits
No real model, credentials or network. Production systems need centralized identity, durable policy revisions, revocation propagation and enforcement at every downstream fetch/tool call.
