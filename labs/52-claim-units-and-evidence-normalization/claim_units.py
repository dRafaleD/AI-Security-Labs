"""Verify fictional numeric claims against host-provided measurements."""
from fractions import Fraction

SCALE = {"B": 1, "KiB": 1024, "MiB": 1048576}
EVIDENCE = {"doc-a": {"size": (2048, "B")}, "doc-b": {"size": (1, "MiB")}}

def check(ref, field, number, unit):
    if ref not in EVIDENCE or field not in EVIDENCE[ref]:
        return "NO_EVIDENCE"
    if type(number) is not int or number < 0 or unit not in SCALE:
        return "INVALID_CLAIM"
    actual, actual_unit = EVIDENCE[ref][field]
    return "SUPPORTED_VALUE" if Fraction(number)*SCALE[unit] == actual*SCALE[actual_unit] else "VALUE_MISMATCH"

def main():
    cases = [
        ("doc-a", "size", 2, "KiB", "SUPPORTED_VALUE"),
        ("doc-a", "size", 2048, "B", "SUPPORTED_VALUE"),
        ("doc-a", "size", 2, "B", "VALUE_MISMATCH"),
        ("doc-a", "size", 2, "KB", "INVALID_CLAIM"),
        ("doc-b", "size", 1024, "KiB", "SUPPORTED_VALUE"),
        ("doc-b", "size", 1000, "KiB", "VALUE_MISMATCH"),
        ("doc-b", "size", True, "MiB", "INVALID_CLAIM"),
        ("doc-a", "size", -1, "B", "INVALID_CLAIM"),
        ("doc-a", "duration", 2, "B", "NO_EVIDENCE"),
        ("missing", "size", 2, "B", "NO_EVIDENCE"),
    ]
    for *args, expected in cases:
        result = check(*args)
        assert result == expected, (args, result)
        print(result)
    print("10/10 claim checks passed")

if __name__ == "__main__":
    main()
