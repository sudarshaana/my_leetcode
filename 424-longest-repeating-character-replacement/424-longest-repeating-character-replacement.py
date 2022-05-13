class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        mC = 0
        dic = {}
        
        for r, subS in enumerate(s):
            dic[subS] = 1+dic.get(subS, 0)
            
            while((r-l+1) - max(dic.values()) > k):
                dic[s[l]] -=1
                l+=1
            mC = max(mC, r-l+1)            
        return mC