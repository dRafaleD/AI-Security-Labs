"""Local fictional assistant output projection; no model or external tools."""
DOC = {"title":"Training notes", "summary":"Fictional report",
       "owner":"alice", "internal_id":"LAB-42", "private_note":"synthetic private data"}
FIELDS = {"reader": {"title","summary"}, "auditor": {"title","summary","internal_id"}}

def project(role, requested, record):
    if role not in FIELDS:
        return "DENY_ROLE", {}
    if not isinstance(requested,list) or not requested:
        return "INVALID_FIELDS", {}
    if any(not isinstance(field,str) for field in requested):
        return "INVALID_FIELDS", {}
    if len(set(requested)) != len(requested):
        return "INVALID_FIELDS", {}
    if any(field not in FIELDS[role] for field in requested):
        return "DENY_FIELD", {}
    if any(field not in record for field in requested):
        return "MISSING_FIELD", {}
    return "DATA_ONLY", {field:record[field] for field in requested}

def main():
    cases = [
        ("reader",["title"],DOC,"DATA_ONLY"),
        ("reader",["title","summary"],DOC,"DATA_ONLY"),
        ("reader",["internal_id"],DOC,"DENY_FIELD"),
        ("reader",["title","private_note"],DOC,"DENY_FIELD"),
        ("auditor",["internal_id"],DOC,"DATA_ONLY"),
        ("auditor",["owner"],DOC,"DENY_FIELD"),
        ("unknown",["title"],DOC,"DENY_ROLE"),
        ("reader",[],DOC,"INVALID_FIELDS"),
        ("reader",["title","title"],DOC,"INVALID_FIELDS"),
        ("reader",[1],DOC,"INVALID_FIELDS"),
        ("reader",["summary"],{},"MISSING_FIELD"),
    ]
    for role,fields,record,expected in cases:
        verdict,out=project(role,fields,record)
        assert verdict==expected,(role,fields,verdict)
        assert set(out)==(set(fields) if verdict=="DATA_ONLY" else set())
        print(role,fields,verdict)
    print("11 projection scenarios passed")

if __name__=="__main__":
    main()
