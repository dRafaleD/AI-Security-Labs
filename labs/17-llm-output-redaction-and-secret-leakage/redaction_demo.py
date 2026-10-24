"""Redact synthetic secret-like strings from model output before display."""
import re

PATTERNS = {
    "api_key": re.compile(r"\bKEY-[A-Z0-9]{8}\b"),
    "email": re.compile(r"\b[\w.+-]+@example\.test\b"),
}

def redact(text):
    findings = []
    for label, pattern in PATTERNS.items():
        text, count = pattern.subn(f"[REDACTED:{label}]", text)
        if count:
            findings.append((label, count))
    return text, findings

if __name__ == "__main__":
    sample = "Contact ops@example.test and use KEY-AB12CD34 for the demo."
    clean, findings = redact(sample)
    print(clean)
    print("findings:", findings)
    assert "KEY-AB12CD34" not in clean
    assert "ops@example.test" not in clean
    print("PASS: synthetic secrets were removed from the displayed output.")
    print("Review: a regex list misses unknown formats; combine with data minimization and logging controls.")
