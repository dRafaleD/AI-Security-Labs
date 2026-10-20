import hashlib,json
def audit(request_id,user_id,action,allowed):
    return {"request_id":request_id,"actor_hash":hashlib.sha256(user_id.encode()).hexdigest()[:12],"action":action,"allowed":bool(allowed)}
if __name__=="__main__":
    entry=audit("r-13","synthetic-user","read_note",True)
    print(json.dumps(entry,sort_keys=True))
    assert "synthetic-user" not in json.dumps(entry)
