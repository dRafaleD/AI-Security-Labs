class Budget:
    def __init__(self,limit):self.limit=limit;self.used=0
    def allow(self):
        if self.used>=self.limit:return False
        self.used+=1;return True
b=Budget(3)
for _ in range(5):print("tool_allowed",b.allow())
assert b.used==3
