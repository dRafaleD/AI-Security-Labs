#!/usr/bin/env python3
"""Offline agent action gate: approval must match the resource's current version."""
from dataclasses import dataclass

@dataclass
class Approval:
    actor: str
    tenant: str
    action: str
    resource: str
    expected_version: int
    expires_at: int
    used: bool = False

RESOURCES = {
    "doc-a": {"tenant": "alpha", "version": 4, "contents": "training"},
}
USER_TENANT = {"alice": "alpha", "bob": "beta"}
APPROVALS = {
    "ap-read": Approval("alice", "alpha", "read", "doc-a", 4, 120),
    "ap-stale": Approval("alice", "alpha", "read", "doc-a", 3, 120),
    "ap-write": Approval("alice", "alpha", "write", "doc-a", 4, 120),
    "ap-exp": Approval("alice", "alpha", "read", "doc-a", 4, 110),
}

def invoke(actor: str, approval_id: str, action: str,
           resource: str, now: int) -> str:
    record = RESOURCES.get(resource)
    tenant = USER_TENANT.get(actor)
    if not record or not tenant or record["tenant"] != tenant:
        return "DENY_SCOPE"
    approval = APPROVALS.get(approval_id)
    if not approval or approval.used or now >= approval.expires_at:
        return "DENY_APPROVAL"
    if (approval.actor, approval.tenant, approval.action, approval.resource) != (
        actor, tenant, action, resource
    ):
        return "DENY_BINDING"
    if approval.expected_version != record["version"]:
        return "DENY_STALE_RESOURCE"
    if action != "read":  # Toy application has no write capability.
        return "DENY_TOOL_POLICY"
    approval.used = True
    return "SIMULATED_READ"

def main():
    cases = [
        ("stale approval", ("alice", "ap-stale", "read", "doc-a", 100), "DENY_STALE_RESOURCE"),
        ("wrong actor", ("bob", "ap-read", "read", "doc-a", 100), "DENY_SCOPE"),
        ("wrong resource", ("alice", "ap-read", "read", "missing", 100), "DENY_SCOPE"),
        ("wrong requested action", ("alice", "ap-read", "write", "doc-a", 100), "DENY_BINDING"),
        ("blocked by tool policy", ("alice", "ap-write", "write", "doc-a", 100), "DENY_TOOL_POLICY"),
        ("expired", ("alice", "ap-exp", "read", "doc-a", 110), "DENY_APPROVAL"),
        ("valid read", ("alice", "ap-read", "read", "doc-a", 100), "SIMULATED_READ"),
        ("approval replay", ("alice", "ap-read", "read", "doc-a", 101), "DENY_APPROVAL"),
    ]
    for label, args, expected in cases:
        actual = invoke(*args)
        assert actual == expected, (label, actual)
        print(f"{label:25} {actual}")
    print("8/8 synthetic approval and version checks passed")

if __name__ == "__main__":
    main()
