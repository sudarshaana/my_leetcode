class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        
        prefix = strs[0]
        
        for st in strs:
            
            new_pref = ""
            
            min_len = min(len(prefix), len(st))
            
            for i in range(min_len):
                if st[i] == prefix[i]:
                    new_pref += st[i]
                else:
                    break
            
            if new_pref == "":
                return ""
            else:
                prefix = new_pref
                
        return prefix