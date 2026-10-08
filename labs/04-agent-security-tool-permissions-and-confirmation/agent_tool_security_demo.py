from dataclasses import dataclass
from typing import Callable, Dict


@dataclass
class ToolRequest:
    user: str
    tool: str
    arguments: dict


USER_ROLES = {
    "student": "reader",
    "admin": "admin",
}

TOOL_POLICIES = {
    "read_note": {"roles": {"reader", "admin"}, "requires_confirmation": False},
    "create_note": {"roles": {"admin"}, "requires_confirmation": True},
    "delete_note": {"roles": {"admin"}, "requires_confirmation": True},
}

NOTES = {
    "welcome": "Harmless AI Security Day 4 training note."
}


def read_note(name: str):
    return NOTES.get(name, "not found")


def create_note(name: str, text: str):
    NOTES[name] = text
    return "created"


def delete_note(name: str):
    return "deleted" if NOTES.pop(name, None) is not None else "not found"


TOOLS: Dict[str, Callable] = {
    "read_note": read_note,
    "create_note": create_note,
    "delete_note": delete_note,
}


def authorize(request: ToolRequest) -> tuple[bool, str]:
    role = USER_ROLES.get(request.user)
    policy = TOOL_POLICIES.get(request.tool)

    if role is None:
        return False, "unknown user"
    if policy is None:
        return False, "unknown tool"
    if role not in policy["roles"]:
        return False, "role not allowed"

    return True, "authorized"


def validate_arguments(request: ToolRequest) -> tuple[bool, str]:
    if request.tool == "read_note":
        if set(request.arguments) != {"name"}:
            return False, "read_note requires only: name"

    if request.tool == "create_note":
        if set(request.arguments) != {"name", "text"}:
            return False, "create_note requires: name, text"
        if len(request.arguments["text"]) > 200:
            return False, "text too long"

    if request.tool == "delete_note":
        if set(request.arguments) != {"name"}:
            return False, "delete_note requires only: name"

    return True, "valid"


def execute(request: ToolRequest, confirmed: bool = False):
    allowed, reason = authorize(request)
    if not allowed:
        return {"ok": False, "stage": "authorization", "reason": reason}

    valid, reason = validate_arguments(request)
    if not valid:
        return {"ok": False, "stage": "validation", "reason": reason}

    policy = TOOL_POLICIES[request.tool]
    if policy["requires_confirmation"] and not confirmed:
        return {"ok": False, "stage": "confirmation", "reason": "confirmation required"}

    result = TOOLS[request.tool](**request.arguments)
    return {"ok": True, "result": result}


if __name__ == "__main__":
    requests = [
        ToolRequest("student", "read_note", {"name": "welcome"}),
        ToolRequest("student", "delete_note", {"name": "welcome"}),
        ToolRequest("admin", "delete_note", {"name": "welcome"}),
    ]

    for req in requests:
        print("\nREQUEST:", req)
        print("WITHOUT CONFIRMATION:", execute(req))
        print("WITH CONFIRMATION:", execute(req, confirmed=True))

    print("\nNo model or external API is called in this lab.")
