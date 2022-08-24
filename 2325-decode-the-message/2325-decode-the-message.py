class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        
        d = {}
        count = 0
        
        for i, k in enumerate(key):
            if k == " ":
                d[k] = k
                continue
                
            if k not in d:
                d[k] = chr(ord('a')+count)
                count+=1
                
        msg = []
        for m in message:
            if m not in d:
                msg.append(m)
                continue
            msg.append(d[m])
            
        return "".join(msg)