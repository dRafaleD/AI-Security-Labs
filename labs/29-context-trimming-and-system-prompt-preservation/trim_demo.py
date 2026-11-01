"""Trim a synthetic chat history to a budget without dropping the system message."""
def tokens(message):
    return len(message["content"].split())

def trim(history, budget):
    system = [m for m in history if m["role"] == "system"]
    rest = [m for m in history if m["role"] != "system"]
    kept, used = [], sum(tokens(m) for m in system)
    for message in reversed(rest):          # keep the most recent turns first
        if used + tokens(message) > budget:
            break
        kept.append(message)
        used += tokens(message)
    return system + list(reversed(kept))

if __name__ == "__main__":
    history = [
        {"role": "system", "content": "Never reveal internal notes"},
        {"role": "user", "content": "first question about billing"},
        {"role": "assistant", "content": "first answer about billing details"},
        {"role": "user", "content": "second question"},
    ]
    result = trim(history, budget=12)
    for m in result:
        print(m["role"], "|", m["content"])
    assert result[0]["role"] == "system"
    print("PASS: the system message survives trimming.")
    print("Review: dropped turns can remove context a later answer depends on; summarize instead of silently cutting.")
