"""Deterministic authorization checks: no LLM or network involved."""
cases=[
 ("reader","a","read","a",True),
 ("reader","a","read","b",False),
 ("reader","a","delete","a",False),
 ("admin","a","delete","a",True),
 ("admin","a","arbitrary_shell","a",False),
]
permissions={"reader":{"read"},"admin":{"read","delete"}}
def allowed(role,tenant,action,target_tenant):
 return tenant==target_tenant and action in permissions.get(role,set())
for role,tenant,action,target,expected in cases:
 actual=allowed(role,tenant,action,target)
 assert actual==expected,(role,tenant,action,target)
 print("PASS",role,action,target)
print("Synthetic policy regression passed; no model resilience was measured.")
