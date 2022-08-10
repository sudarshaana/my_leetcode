class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}
        for item in strs:
            s = ''.join(sorted(item))
            
            if s not in m:
                m[s] = [item]
            else:
                m[s].append(item)
                
        return list(m.values())