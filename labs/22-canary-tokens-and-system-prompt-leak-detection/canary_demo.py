"""Detect verbatim system prompt leakage with a per-session canary token."""
import secrets


def new_session():
    canary = "CANARY-" + secrets.token_hex(8)
    return {"canary": canary, "system_prompt": f"You are a billing assistant. Internal marker: {canary}."}


def leaked(session, output):
    return session["canary"] in output


if __name__ == "__main__":
    a, b = new_session(), new_session()
    outputs = {
        "normal answer": "Your invoice total is 40 EUR.",
        "verbatim leak": "My instructions say: " + a["system_prompt"],
        "paraphrase leak": "I was told I am a billing assistant with an internal marker.",
    }
    for name, text in outputs.items():
        print(f"{name:16} leaked={leaked(a, text)}")
    assert not leaked(a, outputs["normal answer"])
    assert leaked(a, outputs["verbatim leak"])
    assert not leaked(b, outputs["verbatim leak"]), "another session's canary must not match"
    assert a["canary"] != b["canary"]
    print("PASS: a per-session canary detects verbatim leaks and identifies the session.")
    print("Review: paraphrased leaks are not detected; the prompt must never hold secrets.")
