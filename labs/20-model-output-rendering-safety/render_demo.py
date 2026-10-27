"""Render synthetic model output safely: escape HTML and allow only https links."""
import html
import re

LINK = re.compile(r"\[([^\]]+)\]\(((?:[^()\s]|\([^()\s]*\))+)\)")

def render(text):
    escaped = html.escape(text)
    def link(match):
        label, url = match.group(1), html.unescape(match.group(2))
        if url.startswith("https://"):
            return f'<a href="{html.escape(url, quote=True)}" rel="noopener noreferrer">{label}</a>'
        return label  # drop the link, keep the text
    return LINK.sub(link, escaped)

if __name__ == "__main__":
    sample = 'Hello <script>alert(1)</script> [docs](https://example.test/a) [bad](javascript:alert(1))'
    out = render(sample)
    print(out)
    assert "<script>" not in out
    assert "javascript:" not in out
    assert 'href="https://example.test/a"' in out
    print("PASS: markup is escaped and only https links survive.")
    print("Review: this is not a full markdown renderer; test your real renderer and add a Content-Security-Policy.")
