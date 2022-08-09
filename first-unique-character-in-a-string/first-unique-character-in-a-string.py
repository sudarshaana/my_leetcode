from collections import OrderedDict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        #first_occurance = -1
        hash_map = OrderedDict()
        
        
        for i, char in enumerate(s):
            #if not char in hash_map:
            #    hash_map[char]=1
            #else:
            hash_map[char]=hash_map.get(char, 0) + 1
            
        for i, k in enumerate(hash_map.keys()):
            if hash_map[k]==1:
                return s.find(k)
        return -1
    