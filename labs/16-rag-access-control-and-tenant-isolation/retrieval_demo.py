DOCS=[{"tenant":"a","id":"a1","body":"public for tenant a"},{"tenant":"b","id":"b1","body":"private tenant b"}]
def retrieve(tenant,phrase):
    return [d["id"] for d in DOCS if d["tenant"]==tenant and phrase in d["body"]]
assert retrieve("a","private")==[]
assert retrieve("b","private")==["b1"]
print("Tenant-scoped retrieval tests passed")
