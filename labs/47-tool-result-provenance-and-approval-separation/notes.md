# Day 47 — Tool-Result Provenance and Approval Separation

[English](notes.md) · [Türkçe](notes.tr.md) · [Code](approval_boundary.py)

Day 46 scoped a result budget to a trusted epoch. Day 47 separates permission to read a document from text obtained by reading it. The toy controller receives an approval object from its own trusted control plane. The approval binds actor, document and epoch; quoted content can neither create nor enlarge that grant. A valid decision is READ_DATA_ONLY, never a command dispatch.

**Questions:** Why does an authorized read not authorize a later write? Why should approval metadata be distinct from retrieved text? What happens when an approval's epoch changes?

This models only a trusted in-process approval object, not an authenticated token, one-time grant or production agent. No LLM, external API, filesystem changes or real tool execution.

## Run
```bash
python3 labs/47-tool-result-provenance-and-approval-separation/approval_boundary.py
```
