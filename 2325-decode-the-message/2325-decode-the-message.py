class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        
        d = {}
        d[" "] = " "
        count = 0
        
        for i, k in enumerate(key):
            if k not in d:
                d[k] = chr(ord('a')+count)
                count+=1
                
        msg = []
        for m in message:
            msg.append(d[m])
            
        return "".join(msg)