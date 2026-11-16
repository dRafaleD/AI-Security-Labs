# Day 39 — RAG Cache Integrity and Untrusted Content

[English](notes.md) · [Türkçe](notes.tr.md) · [Offline Python exercise](cache_integrity_demo.py)

## Day 38 follow-up
A cache can obey TTL and document versions and **still return modified content** if its stored bytes are changed. This lab explores how to reject corrupted cached text before it reaches a retrieval-augmented-generation (RAG) model.

## Defense in depth
A fictional cache entry stores document text, SHA-256, document version, policy revision and expiry. Before serving it:
1. **Authorize** the current principal and tenant against an application-controlled record.
2. Verify the TTL, policy revision and current document version.
3. Compare the cached text's digest with the cached digest **and the authoritative document's digest**.
4. Refresh from the authoritative in-memory source on any mismatch.

The test corrupts cache text, then corrupts both text and its cached hash. Both are rejected because the independent source differs. Version changes, expiry, cross-tenant access and authorization revocation are also tested.

## Run
~~~bash
python3 labs/39-rag-cache-integrity-and-untrusted-content/cache_integrity_demo.py
~~~

## Important limitations
The “authoritative” source is a hardcoded toy dictionary. A real document store can itself be compromised; checksums are **not** signatures or provenance guarantees. Hash comparison cannot establish whether content is true or whether its instructions should be obeyed. Retrieved text always remains **data**, never system-level instructions.

## Questions
1. Why doesn't recomputing only the cached digest provide a trust anchor?
2. What changes if a malicious actor controls both cache and source registry?
3. Why is tenant authorization required before every cache hit?
4. Where should an application validate permissions when a retrieved document is used to invoke a tool?
5. What is the difference between byte integrity, source authorization and semantic correctness?
