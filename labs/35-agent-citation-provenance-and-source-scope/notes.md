# Day 35 — Agent Citations, Source Provenance and Scope

[English](notes.md) · [Türkçe](notes.tr.md) · [Offline citation guard](citation_guard_demo.py)

## Continue from untrusted tool outputs
Day 34 limited tool response size and kept retrieved text separate from trusted control metadata. Today we ask what happens when an agent **cites** that text. A citation such as doc-a looks convincing, but a model can invent source identifiers or accidentally cite a document that belongs to another tenant.

**Citation presence is not evidence quality.** A legitimate identifier does not guarantee the source is accurate or that the source actually supports the sentence being cited.

## Controller-side checks
The toy controller stores a trusted-for-this-exercise document registry with **server-assigned IDs**, tenant scopes and digests pinned to known bytes. It then checks:
1. Every cited ID was actually present in the specific retrieved set.
2. Every retrieved item belongs to the calling tenant's approved scope.
3. Retrieved bytes match the registered SHA-256 digest.
4. Source text remains **untrusted content** even after those structural checks. Embedded instructions such as SYSTEM: ignore rules have no authority.
5. Citation checks **do not** prove semantic support for a claim; real applications still need claim-to-source grounding and independent review.

A checksum can detect a change compared with the pinned snapshot. It does not independently establish authorship, authenticity, factual accuracy or correct tenant configuration.

## Run
~~~bash
python3 citation_guard_demo.py
~~~

No LLM, web requests, credentials or real documents. The script tests an authorized citation, a fabricated ID, a cross-tenant reference, altered bytes and a record containing a fictional instruction line. It asserts expected outcomes and never executes text found in a document.

## Exercises
1. Why is a citation ID chosen by the model less trustworthy than a server-provided document reference?
2. Explain the difference between **integrity**, **provenance**, **authorization** and **grounding**.
3. Modify a document byte and see why the pinned digest check fails.
4. Which type of false confidence might arise when a real citation points to irrelevant text?
5. How would you validate a generated claim against an exact quoted passage, including limits on quoting and paraphrase?
6. In a multi-tenant RAG service, which boundary prevents team A from citing team B's retrieved documents?

## Limits
A Python dictionary is not a secure source registry. In production, authenticate the retrieval backend, validate metadata at the trust boundary, restrict per-user permissions, prevent stale/source ID reuse and log provenance without storing unnecessary sensitive text. Passing this demo's checks does not make an AI answer safe or true.
