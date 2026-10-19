docs={"a1":("tenant-a","Reset requires a one-time token."),"b1":("tenant-b","Private record.")}
def check(tenant,doc_id,phrase):
    record=docs.get(doc_id)
    return bool(record and record[0]==tenant and phrase.lower() in record[1].lower())
assert check("tenant-a","a1","one-time token")
assert not check("tenant-a","b1","private")
assert not check("tenant-a","a1","never expires")
print("Three local provenance checks passed.")
