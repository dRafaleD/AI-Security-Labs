from dataclasses import dataclass
@dataclass(frozen=True)
class Request:
    user: str
    action: str
    note: str
    request_id: str

seen=set()
notes={}
def execute(req, approved=False):
    if req.user != "admin": return "DENY: role"
    if req.action != "create_note": return "DENY: action"
    if not isinstance(req.note,str) or len(req.note)>100: return "DENY: args"
    if not approved: return "DENY: confirmation"
    if req.request_id in seen: return "REPLAY: already applied"
    seen.add(req.request_id)
    notes[req.request_id]=req.note
    return "CREATED"

if __name__=="__main__":
    r=Request("admin","create_note","Synthetic example","req-001")
    print(execute(r))
    print(execute(r,True))
    print(execute(r,True))
    print(notes)
