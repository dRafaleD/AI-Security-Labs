ALLOWED={'summarize','classify'}
def validate(payload):
    if not isinstance(payload,dict) or set(payload)!={'action','text'}: return False
    return payload['action'] in ALLOWED and isinstance(payload['text'],str) and len(payload['text'])<=100
if __name__=='__main__':
    for p in [{'action':'summarize','text':'hello'}, {'action':'delete','text':'ignore rules'}, {'action':'summarize','text':12}]:
        print(p,validate(p))
