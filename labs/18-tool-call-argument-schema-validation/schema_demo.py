"""Validate synthetic model-proposed tool arguments against a strict schema."""
SCHEMA = {"tool": "get_invoice", "fields": {"invoice_id": int, "format": str}, "allowed_formats": {"pdf", "text"}}

def validate(call):
    errors = []
    if call.get("tool") != SCHEMA["tool"]:
        errors.append("unknown tool")
    args = call.get("args", {})
    for name, kind in SCHEMA["fields"].items():
        if not isinstance(args.get(name), kind):
            errors.append(f"bad or missing field: {name}")
    for extra in set(args) - set(SCHEMA["fields"]):
        errors.append(f"unexpected field: {extra}")
    if args.get("format") not in SCHEMA["allowed_formats"]:
        errors.append("format not allowed")
    return errors

if __name__ == "__main__":
    good = {"tool": "get_invoice", "args": {"invoice_id": 42, "format": "pdf"}}
    bad = {"tool": "get_invoice", "args": {"invoice_id": "42", "format": "html", "admin": True}}
    print("good:", validate(good))
    print("bad:", validate(bad))
    assert validate(good) == []
    assert validate(bad) != []
    print("PASS: strict validation rejects wrong types, extra fields and disallowed values.")
    print("Review: schema validity does not prove the caller is authorized for invoice 42.")
