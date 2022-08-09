class Solution:
    
    
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        return self.encode(s) == self.encode(t)
    
    def encode(self, st):
        d = {}
        return str([d.setdefault(c,len(d)) for c in st])
    
#         hashmap = {}
        
#         for i, char in enumerate(s):
#             if char in hashmap:
#                 if hashmap[char] != t[i]:
#                     return False
#             else:
#                 hashmap[char] = t[i]
        
#         if len(hashmap.keys()) != len(set(t)):
#             return False
#         return True

    