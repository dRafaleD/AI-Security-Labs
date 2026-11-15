#!/usr/bin/env python3
"""Offline RAG cache: policy, document version and TTL checks before disclosure."""
DOCUMENTS = {
    "alpha-guide": {"tenant": "alpha", "groups": {"reader"}, "version": 1, "text": "Training note v1"},
    "beta-guide": {"tenant": "beta", "groups": {"reader"}, "version": 1, "text": "Other tenant text"},
}
USERS = {"alice": {"tenant": "alpha", "groups": {"reader"}, "revision": 1}}
CACHE = {}
TTL = 10

def permitted(user: str, doc: str) -> bool:
    actor, record = USERS.get(user), DOCUMENTS.get(doc)
    return bool(actor and record and actor["tenant"] == record["tenant"]
                and bool(actor["groups"] & record["groups"]))

def fetch(user: str, doc: str, now: int) -> str | None:
    if not permitted(user, doc):
        return None  # Authorize before cache access.
    actor, record = USERS[user], DOCUMENTS[doc]
    key = (user, doc)
    hit = CACHE.get(key)
    if (hit and now < hit["expires_at"]
            and hit["policy_revision"] == actor["revision"]
            and hit["document_version"] == record["version"]):
        return hit["text"]
    CACHE[key] = {
        "text": record["text"], "expires_at": now + TTL,
        "policy_revision": actor["revision"],
        "document_version": record["version"],
    }
    return record["text"]

def main():
    passed = 0
    def check(value):
        nonlocal passed
        assert value
        passed += 1

    check(fetch("alice", "alpha-guide", 100) == "Training note v1")
    check(fetch("alice", "alpha-guide", 103) == "Training note v1")
    check(CACHE[("alice", "alpha-guide")]["expires_at"] == 110)
    check(fetch("alice", "beta-guide", 104) is None)
    DOCUMENTS["alpha-guide"]["version"] = 2
    DOCUMENTS["alpha-guide"]["text"] = "Training note v2"
    check(fetch("alice", "alpha-guide", 105) == "Training note v2")
    check(CACHE[("alice", "alpha-guide")]["document_version"] == 2)
    check(fetch("alice", "alpha-guide", 115) == "Training note v2")
    check(CACHE[("alice", "alpha-guide")]["expires_at"] == 125)
    USERS["alice"]["groups"].clear()
    USERS["alice"]["revision"] += 1
    check(fetch("alice", "alpha-guide", 116) is None)
    check(fetch("unknown", "alpha-guide", 116) is None)
    print(f"{passed}/{passed} RAG cache assertions passed; no LLM or network used")

if __name__ == "__main__":
    main()
