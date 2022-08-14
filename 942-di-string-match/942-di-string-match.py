class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        
        l, h = 0, len(s)
        res = []
        
        for i, c in enumerate(s):
            
            if c == "I":
                res.append(l)
                l+=1
            else:
                res.append(h)
                h-=1
                
        return res+[l]