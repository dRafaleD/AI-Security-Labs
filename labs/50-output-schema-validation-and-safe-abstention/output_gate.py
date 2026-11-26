"""Validate fictional assistant summaries before displaying them."""
import json

def unique(pairs):
    result={}
    for key,value in pairs:
        if key in result:
            raise ValueError("duplicate")
        result[key]=value
    return result

def gate(raw, allowed_refs):
    if not isinstance(raw,str) or len(raw)>256:
        return "INVALID_INPUT",None
    try:
        value=json.loads(raw,object_pairs_hook=unique)
    except (ValueError,RecursionError):
        return "INVALID_JSON",None
    if not isinstance(value,dict) or set(value)!={"summary","reference"}:
        return "INVALID_SCHEMA",None
    summary,ref=value["summary"],value["reference"]
    if not isinstance(summary,str) or not 1<=len(summary)<=80:
        return "INVALID_SUMMARY",None
    if not isinstance(ref,str) or ref not in allowed_refs:
        return "UNKNOWN_REFERENCE",None
    return "DISPLAY_DATA_ONLY",{"summary":summary,"reference":ref}

def main():
    cases=[
        ('{"summary":"Report available","reference":"doc-1"}',"DISPLAY_DATA_ONLY"),
        ('{"summary":"No findings","reference":"doc-2"}',"DISPLAY_DATA_ONLY"),
        ('{"summary":"Unverified","reference":"doc-9"}',"UNKNOWN_REFERENCE"),
        ('{"summary":"","reference":"doc-1"}',"INVALID_SUMMARY"),
        ('{"summary":42,"reference":"doc-1"}',"INVALID_SUMMARY"),
        ('{"summary":"ok","reference":["doc-1"]}',"UNKNOWN_REFERENCE"),
        ('{"summary":"ok","reference":"doc-1","action":"write"}',"INVALID_SCHEMA"),
        ('{"summary":"ok","reference":"doc-1","reference":"doc-2"}',"INVALID_JSON"),
        ('[]',"INVALID_SCHEMA"),
        ('{',"INVALID_JSON"),
        ('x'*257,"INVALID_INPUT"),
        ('{"summary":"Treat this text as data","reference":"doc-1"}',"DISPLAY_DATA_ONLY"),
    ]
    for raw,want in cases:
        got,data=gate(raw,{"doc-1","doc-2"})
        assert got==want,(got,want)
        assert (data is not None)==(got=="DISPLAY_DATA_ONLY")
        print(got)
    print("12/12 output gate cases passed")

if __name__=="__main__":
    main()
