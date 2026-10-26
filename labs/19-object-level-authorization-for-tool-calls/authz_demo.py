"""A schema-valid model tool call still needs an object-level authorization check."""
INVOICES = {1: {"owner": "alice", "total": 40}, 2: {"owner": "bob", "total": 99}}


def get_invoice(session_user, call):
    invoice_id = call["args"]["invoice_id"]          # model-proposed, untrusted
    invoice = INVOICES.get(invoice_id)
    if invoice is None or invoice["owner"] != session_user:
        return {"error": "not found"}                # same answer for missing and forbidden
    return invoice


if __name__ == "__main__":
    own = {"tool": "get_invoice", "args": {"invoice_id": 1}}
    other = {"tool": "get_invoice", "args": {"invoice_id": 2}}
    missing = {"tool": "get_invoice", "args": {"invoice_id": 999}}
    print("own    :", get_invoice("alice", own))
    print("other  :", get_invoice("alice", other))
    print("missing:", get_invoice("alice", missing))
    assert get_invoice("alice", own)["total"] == 40
    assert get_invoice("alice", other) == get_invoice("alice", missing)
    print("PASS: authorization uses the session user, not anything the model wrote.")
    print("Review: the prompt cannot be the only control; this check lives in the tool.")
