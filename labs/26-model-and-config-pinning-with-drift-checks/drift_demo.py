"""Fingerprint a model config in canonical form and detect drift from an approved value."""
import hashlib
import json

APPROVED = {"model": "assistant-v1.4.2", "temperature": 0.2, "tools": ["search"], "max_tokens": 800}


def fingerprint(cfg):
    canonical = json.dumps(cfg, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(canonical.encode()).hexdigest()[:16]


def drifted(cfg):
    return fingerprint(cfg) != fingerprint(APPROVED)


if __name__ == "__main__":
    reordered = {"max_tokens": 800, "tools": ["search"], "temperature": 0.2, "model": "assistant-v1.4.2"}
    added_tool = dict(APPROVED, tools=["search", "shell"])
    alias = dict(APPROVED, model="assistant-latest")
    for name, cfg in (("approved", APPROVED), ("reordered", reordered), ("added tool", added_tool), ("alias", alias)):
        print(f"{name:11} {fingerprint(cfg)} drifted={drifted(cfg)}")
    assert not drifted(reordered)
    assert drifted(added_tool) and drifted(alias)
    print("PASS: key order is ignored, while any real change is detected.")
    print("Review: an unchanged hash does not prove the approved config is safe.")
