"""Deterministic agent plan controller; authorizations checked per proposed step."""
from dataclasses import dataclass

@dataclass(frozen=True)
class Step:
    principal: str
    action: str
    resource: str

# Exact resource identities; no wildcard or implicit trust.
PERMISSIONS = {
    ("analyst", "read", "doc:public-overview"),
    ("analyst", "summarize", "doc:public-overview"),
}

def authorize(step: Step) -> bool:
    return (step.principal, step.action, step.resource) in PERMISSIONS

def review(plan: list[Step]) -> list[bool]:
    # This function returns policy decisions. It does NOT run any tools.
    return [authorize(step) for step in plan]

plan = [
    Step("analyst", "read", "doc:public-overview"),
    Step("analyst", "export", "doc:public-overview"),
    Step("analyst", "read", "doc:private-report"),
    Step("analyst", "summarize", "doc:public-overview"),
]
expected = [True, False, False, True]
actual = review(plan)
assert actual == expected

for step, allowed in zip(plan, actual):
    print(f"{step.principal}: {step.action} {step.resource} -> "
          f"{'PERMIT' if allowed else 'DENY'}")

# An agent may propose new resource IDs, but that never changes permission.
assert not authorize(Step("analyst", "read", "doc:private-report"))
print("Four per-step decisions verified. No actions executed.")
