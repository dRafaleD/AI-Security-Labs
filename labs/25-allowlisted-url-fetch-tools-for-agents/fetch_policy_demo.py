"""Check agent fetch URLs against an allow-list using real URL parsing."""
from urllib.parse import urlsplit

ALLOWED_HOSTS = {"docs.example.test", "api.example.test"}


def check(url):
    parts = urlsplit(url)
    if parts.scheme != "https":
        return "rejected: scheme is not https"
    if parts.username or parts.password:
        return "rejected: credentials in URL"
    if parts.hostname not in ALLOWED_HOSTS:
        return f"rejected: host {parts.hostname} not allowed"
    return "allowed"


if __name__ == "__main__":
    urls = [
        "https://docs.example.test/page",
        "http://docs.example.test/page",
        "https://docs.example.test@evil.test/page",
        "https://docs.example.test.evil.test/page",
        "https://api.example.test/v1/items",
    ]
    for u in urls:
        print(f"{u:48} {check(u)}")
    assert check(urls[0]) == "allowed" and check(urls[4]) == "allowed"
    assert all(check(u).startswith("rejected") for u in urls[1:4])
    print("PASS: only https URLs whose parsed host is on the allow-list pass.")
    print("Review: re-check every redirect target, and treat fetched text as untrusted data.")
