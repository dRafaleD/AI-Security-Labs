"""Mask synthetic personal data before logging, keeping a short correlation fingerprint."""
import hashlib
import re

EMAIL = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")
CARD = re.compile(r"\b(?:\d[ -]?){13,16}\b")


def fingerprint(value):
    return hashlib.sha256(value.encode()).hexdigest()[:8]


def mask(text):
    text = EMAIL.sub(lambda m: f"<email:{fingerprint(m.group())}>", text)
    return CARD.sub("<card>", text)


if __name__ == "__main__":
    line = "user alice@example.test paid with 4111 1111 1111 1111; retry for alice@example.test"
    masked = mask(line)
    print(masked)
    assert "alice@example.test" not in masked and "4111" not in masked
    assert masked.count("<email:") == 2
    parts = [p for p in masked.split() if p.startswith("<email:")]
    assert parts[0] == parts[1], "same value must keep the same fingerprint"
    print("PASS: values are masked, and repeated values stay correlatable.")
    print("Review: regexes miss free-form names; decide what to log instead of cleaning afterward.")
