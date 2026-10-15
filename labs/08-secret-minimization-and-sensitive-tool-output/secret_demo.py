from dataclasses import dataclass
@dataclass
class Document:
 owner:str
 title:str
 text:str
 api_key:str
record=Document("alice","Guide","Synthetic training content","FAKE_CREDENTIAL_000")
def model_context(user,obj):
 if user!=obj.owner:return {"error":"not authorized"}
 return {"title":obj.title,"text":obj.text}
allowed=model_context("alice",record)
assert "api_key" not in allowed and "FAKE_CREDENTIAL_000" not in str(allowed)
assert model_context("bob",record)=={"error":"not authorized"}
print("PASS tool-response minimization and ownership checks")