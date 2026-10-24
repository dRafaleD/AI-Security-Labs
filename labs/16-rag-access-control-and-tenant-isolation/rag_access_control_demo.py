"""Local synthetic retrieval exercise showing per-workspace filtering."""
RECORDS = [
    {"id": "doc-a", "workspace": "alpha", "text": "blue deployment guide"},
    {"id": "doc-b", "workspace": "beta", "text": "green deployment guide"},
    {"id": "doc-c", "workspace": "alpha", "text": "rotate example keys"},
]

def search(query, workspace):
    terms = set(query.lower().split())
    # Restrict the candidate set to the caller's workspace first.
    candidates = [r for r in RECORDS if r["workspace"] == workspace]
    return [r for r in candidates if terms.intersection(r["text"].lower().split())]

if __name__ == "__main__":
    results = search("deployment", "alpha")
    for item in results:
        print(item["id"], item["text"])
    assert all(item["workspace"] == "alpha" for item in results)
    print("PASS: results remain within the selected workspace.")
    print("Review: apply equivalent scope checks to vector search, caches, and tool results.")
