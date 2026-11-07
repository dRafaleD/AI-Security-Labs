"""Offline action approval gate; no LLM, tools or network."""
from dataclasses import dataclass
import hashlib
import json

def fingerprint(action, arguments):
    data = json.dumps([action, arguments], sort_keys=True, separators=(",",":"))
    return hashlib.sha256(data.encode()).hexdigest()

@dataclass
class Approval:
    digest: str
    expires_at: int
    used: bool = False

def consume(approval, action, arguments, now):
    if approval.used or now >= approval.expires_at:
        return False
    if approval.digest != fingerprint(action,arguments):
        return False
    approval.used = True
    return True

approval = Approval(fingerprint("export", {"resource":"demo-report"}), 120)
assert not consume(approval,"export",{"resource":"other-report"},110)
assert consume(approval,"export",{"resource":"demo-report"},110)
assert not consume(approval,"export",{"resource":"demo-report"},111)
expired = Approval(fingerprint("view",{}), 50)
assert not consume(expired,"view",{},50)
print("Argument-bound, single-use approval checks passed.")
