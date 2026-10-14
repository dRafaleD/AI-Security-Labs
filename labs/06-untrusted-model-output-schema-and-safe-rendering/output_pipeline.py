"""Local LLM-output security simulation. No actual model, browser or API."""
import html
import json

NOTES={"welcome":"Welcome to the harmless AI Security Lab 6.",
       "training":"Sample note with <script>alert('not executed')</script> as text."}
ALLOWED={"read_note","archive_note"}

class OutputError(ValueError):
    pass

def parse_model_action(raw: str) -> dict:
    if not isinstance(raw,str) or len(raw)>1000:
        raise OutputError("invalid output size")
    try:
        obj=json.loads(raw)
    except (json.JSONDecodeError,TypeError) as exc:
        raise OutputError("not valid JSON") from exc
    if type(obj) is not dict or set(obj)!={"action","note_id"}:
        raise OutputError("unexpected schema")
    if type(obj["action"]) is not str or obj["action"] not in ALLOWED:
        raise OutputError("unknown action")
    if type(obj["note_id"]) is not str or obj["note_id"] not in NOTES:
        raise OutputError("unknown note")
    return obj

def execute(raw: str, authenticated_role: str, confirmed: bool=False) -> dict:
    """Authenticated role and confirmation are trusted application inputs, NOT LLM fields."""
    try:
        action=parse_model_action(raw)
    except OutputError as exc:
        return {"ok":False,"reason":str(exc)}
    name=action["note_id"]
    if action["action"]=="read_note":
        # Escaping is context-specific: good for HTML text nodes, not URLs or JS.
        return {"ok":True,"html_text":html.escape(NOTES[name],quote=True)}
    if authenticated_role!="admin":
        return {"ok":False,"reason":"unauthorized"}
    if not confirmed:
        return {"ok":False,"reason":"confirmation required"}
    # Harmless simulation only: no filesystem write or external action.
    return {"ok":True,"result":f"SIMULATED archive of {name}"}

if __name__=="__main__":
    proposals=[
        '{"action":"read_note","note_id":"training"}',
        '{"action":"archive_note","note_id":"welcome"}',
        '{"action":"read_note","note_id":"welcome","role":"admin"}',
        '{"action":"shell","note_id":"welcome"}',
        "not JSON",
    ]
    for item in proposals:
        print("proposal:",item)
        print("result:",execute(item,authenticated_role="reader"))
    print("Admin without confirmation:",execute(proposals[1],authenticated_role="admin"))
    print("Admin with confirmation:",execute(proposals[1],authenticated_role="admin",confirmed=True))
