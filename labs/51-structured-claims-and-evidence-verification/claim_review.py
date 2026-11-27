"""Verify fictional structured claims against a host-controlled fact registry."""
FACTS={"doc-1":{"status":"ready","count":3},
       "doc-2":{"status":"pending","count":0}}

def review(claim,allowed):
    if not isinstance(claim,dict) or set(claim)!={"reference","field","value"}:
        return "INVALID_SCHEMA"
    ref,field,value=claim["reference"],claim["field"],claim["value"]
    if not isinstance(ref,str) or ref not in allowed or ref not in FACTS:
        return "UNKNOWN_REFERENCE"
    if not isinstance(field,str) or field not in FACTS[ref]:
        return "UNKNOWN_FIELD"
    fact=FACTS[ref][field]
    if type(value) is not type(fact):
        return "TYPE_MISMATCH"
    return "SUPPORTED" if value==fact else "ABSTAIN_CONFLICT"

def main():
    def claim(ref,field,value):
        return {"reference":ref,"field":field,"value":value}
    cases=[
        (claim("doc-1","status","ready"),"SUPPORTED"),
        (claim("doc-1","count",3),"SUPPORTED"),
        (claim("doc-1","count",4),"ABSTAIN_CONFLICT"),
        (claim("doc-1","count",3.0),"TYPE_MISMATCH"),
        (claim("doc-1","count",True),"TYPE_MISMATCH"),
        (claim("doc-2","status","pending"),"UNKNOWN_REFERENCE"),
        (claim("missing","status","ready"),"UNKNOWN_REFERENCE"),
        (claim("doc-1","owner","alice"),"UNKNOWN_FIELD"),
        ({"reference":"doc-1"},"INVALID_SCHEMA"),
        ({**claim("doc-1","count",3),"action":"write"},"INVALID_SCHEMA"),
    ]
    for value,want in cases:
        got=review(value,{"doc-1"})
        assert got==want,(got,want)
        print(got)
    print("10/10 structured claim cases passed")

if __name__=="__main__":
    main()
