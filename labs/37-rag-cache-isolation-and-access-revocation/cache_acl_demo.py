#!/usr/bin/env python3
"""Offline retrieval-cache authorization; no LLM or external services."""
DOCS = {
    "a-open": ("alpha", frozenset({"readers"}), "Harmless team notes"),
    "a-admin": ("alpha", frozenset({"admins"}), "Fictional admin memo"),
    "b-open": ("beta", frozenset({"readers"}), "Other fictional tenant"),
}
POLICY = {
    "alice": ("alpha", {"readers"}),
    "root-a": ("alpha", {"admins"}),
    "bob": ("beta", {"readers"}),
}
REVISION = {"alice": 1, "root-a": 1, "bob": 1}
CACHE: dict[tuple, str] = {}

def permitted(user: str, doc_id: str) -> bool:
    principal = POLICY.get(user)
    doc = DOCS.get(doc_id)
    return bool(principal and doc and principal[0] == doc[0] and
                principal[1].intersection(doc[1]))

def fetch(user: str, doc_id: str) -> str | None:
    # Always authorize against current application policy, including cache hits.
    if not permitted(user, doc_id):
        return None
    key = (user, doc_id, REVISION[user])
    if key not in CACHE:
        CACHE[key] = DOCS[doc_id][2]
    return CACHE[key]

def revoke_reader(user: str) -> None:
    tenant, groups = POLICY[user]
    POLICY[user] = (tenant, groups - {"readers"})
    REVISION[user] += 1

def main():
    assert fetch("alice", "a-open") == "Harmless team notes"
    assert fetch("alice", "a-open") == "Harmless team notes"
    assert fetch("alice", "a-admin") is None
    assert fetch("alice", "b-open") is None
    assert fetch("bob", "b-open") == "Other fictional tenant"
    assert fetch("root-a", "a-admin") == "Fictional admin memo"
    revoke_reader("alice")
    assert fetch("alice", "a-open") is None
    assert len(CACHE) == 3  # an old entry can exist but is no longer served
    print("8/8 synthetic cache and revocation assertions passed")

if __name__ == "__main__":
    main()
