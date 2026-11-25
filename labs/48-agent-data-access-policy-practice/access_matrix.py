"""Defensive data access matrix for an imaginary assistant. No actual tools."""
from dataclasses import dataclass

@dataclass(frozen=True)
class Document:
    tenant: str
    classification: str
    owner: str

DOCS = {
    "handbook": Document("alpha","public","alice"),
    "report": Document("alpha","internal","alice"),
    "private": Document("alpha","restricted","alice"),
    "other": Document("beta","internal","carol"),
}
USERS = {"alice":("alpha","member"),"bob":("alpha","member"),
         "carol":("beta","member"),"auditor":("alpha","auditor")}

def decision(actor, document, action, current_approval=False):
    if actor not in USERS or document not in DOCS:
        return "DENY_UNKNOWN"
    tenant, role = USERS[actor]
    target = DOCS[document]
    if tenant != target.tenant:
        return "DENY_TENANT"
    if action not in {"read","summarize"}:
        return "DENY_ACTION"
    if target.classification == "restricted":
        if actor != target.owner:
            return "DENY_RESTRICTED"
        if current_approval is not True:
            return "NEEDS_APPROVAL"
    if role == "auditor" and action == "summarize":
        return "DENY_ROLE"
    return "ALLOW_DATA_ONLY"

def main():
    cases = [
        ("alice","handbook","read",False,"ALLOW_DATA_ONLY"),
        ("bob","report","summarize",False,"ALLOW_DATA_ONLY"),
        ("alice","private","read",False,"NEEDS_APPROVAL"),
        ("alice","private","read",True,"ALLOW_DATA_ONLY"),
        ("alice","private","read","yes","NEEDS_APPROVAL"),
        ("bob","private","read",True,"DENY_RESTRICTED"),
        ("alice","other","read",True,"DENY_TENANT"),
        ("carol","other","summarize",False,"ALLOW_DATA_ONLY"),
        ("carol","report","read",False,"DENY_TENANT"),
        ("alice","report","delete",True,"DENY_ACTION"),
        ("alice","handbook","export",True,"DENY_ACTION"),
        ("auditor","report","read",False,"ALLOW_DATA_ONLY"),
        ("auditor","report","summarize",False,"DENY_ROLE"),
        ("unknown","report","read",True,"DENY_UNKNOWN"),
        ("alice","missing","read",True,"DENY_UNKNOWN"),
    ]
    for *args, expected in cases:
        actual=decision(*args)
        assert actual==expected,(args,actual)
        print(f"{args[0]:8} {args[1]:10} {args[2]:10} {actual}")
    print(f"{len(cases)}/{len(cases)} access-policy cases passed")

if __name__=="__main__":
    main()
