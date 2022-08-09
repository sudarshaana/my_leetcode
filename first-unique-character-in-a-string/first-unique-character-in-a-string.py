from collections import OrderedDict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        hash_map = OrderedDict()
        index = {}
        
        for i, char in enumerate(s):
            hash_map[char]=hash_map.get(char, 0) + 1
            index[char]=i
            
        for i, k in enumerate(hash_map.keys()):
            if hash_map[k]==1:
                return index[k]
        
        return -1
        
#         hash_map = OrderedDict()
        
#         for i, char in enumerate(s):
#             hash_map[char]=hash_map.get(char, 0) + 1
            
#         for i, k in enumerate(hash_map.keys()):
#             if hash_map[k]==1:
#                 return s.find(k)
#         return -1

    