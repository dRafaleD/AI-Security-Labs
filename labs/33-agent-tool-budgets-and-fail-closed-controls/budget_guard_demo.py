#!/usr/bin/env python3
"""Deterministic AI-agent tool policy; does not invoke any actual tool."""
from dataclasses import dataclass

TOOL_COST = {"search_index": 2, "read_document": 1}
ALLOWED_RESOURCE = "own-notes"


@dataclass
class BudgetGuard:
    max_calls: int = 2
    max_cost: int = 3
    used_calls: int = 0
    used_cost: int = 0

    def authorize(self, tool: str, resource: str) -> tuple[bool, str]:
        if tool not in TOOL_COST:
            return False, "tool not permitted"
        if resource != ALLOWED_RESOURCE:
            return False, "resource outside authorized scope"
        if self.used_calls + 1 > self.max_calls:
            return False, "session call limit exceeded"
        cost = TOOL_COST[tool]
        if self.used_cost + cost > self.max_cost:
            return False, "session cost budget exceeded"

        # This simple local counter is NOT concurrency-safe.
        self.used_calls += 1
        self.used_cost += cost
        return True, "policy decision accepted; no tool was executed"


def main() -> None:
    guard = BudgetGuard()
    cases = [
        ("search_index", "own-notes", True),
        ("read_document", "own-notes", True),
        ("search_index", "own-notes", False),
        ("export_data", "own-notes", False),
        ("read_document", "other-user-notes", False),
    ]
    for tool, resource, expected in cases:
        accepted, reason = guard.authorize(tool, resource)
        print(f"{tool:15} {resource:16} "
              f"{'ALLOW' if accepted else 'DENY':5} | {reason}")
        assert accepted is expected, (tool, resource, reason)
    assert (guard.used_calls, guard.used_cost) == (2, 3)

    # Separate cost limit from call-count limit.
    limited = BudgetGuard(max_calls=3, max_cost=2)
    accepted, _ = limited.authorize("search_index", "own-notes")
    assert accepted
    accepted, reason = limited.authorize("read_document", "own-notes")
    assert not accepted and "cost" in reason
    print("All decisions verified. Production quotas need atomic storage.")


if __name__ == "__main__":
    main()
