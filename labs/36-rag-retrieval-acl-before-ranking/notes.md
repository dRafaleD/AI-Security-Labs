# Day 36 — RAG Retrieval ACLs Before Ranking

[English](notes.md) · [Türkçe](notes.tr.md) · [Python practice](rag_acl_demo.py)

## Why this follows Day 35
Day 35 checked citation provenance and source scope *after retrieval*. Day 36 asks a more basic question: **which documents should enter retrieval at all?** A RAG (retrieval-augmented generation) pipeline must enforce tenant and group-level access before ranking or passing text into an LLM.

**ACL (access control list):** a rule defining who may access a resource. **Tenant:** a separated customer or workspace boundary. **Top-k:** the most highly scored k documents. **Fail closed:** return nothing when access cannot be established.

## Model
Four fictional text records have a tenant, allowed groups, ranking score and data. One belongs to another tenant, one requires administrator access and one contains a prompt-injection-looking sentence. That sentence is **data**, not a command.

The secure sequence is: authenticate principal upstream → derive trusted tenant/groups → **filter authorized documents** → rank only those → pass evidence to the model → validate citations/claims separately.

The exercise contrasts **filter then rank** with **rank global top-1 then filter**. The latter may return no result despite an authorized document existing; it illustrates a recall defect. Filtering the result still prevents this toy example from leaking the other tenant's text, but ranking globally can itself create privacy risks if scores or metadata become visible.

## Run locally
~~~bash
python3 labs/36-rag-retrieval-acl-before-ranking/rag_acl_demo.py
~~~
No API calls, tokens, real documents or model requests.

## Exercises
1. Why must tenant and group identity come from the application, not a model-generated prompt?
2. What happens when the user loses an ACL group between retrieval and disclosure?
3. Why does correct document access not prove that the cited text supports a generated claim?
4. Why should a document's instruction-like phrase never become a system instruction?
5. What would a production system need for index-level isolation, revocation and auditability?

## Boundaries
This is a deterministic ACL demonstration, not a full search or authorization engine. Deny-by-default retrieval does not replace policy enforcement at document download or tool execution.
