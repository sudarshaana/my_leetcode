class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
#         pattern_dict = {}
#         pat = ""
#         for char in pattern:
#             if char in pattern_dict:
#                 pat += pattern_dict[char]
#             else:
#                 pattern_dict[char] = str(len(pattern_dict)+1)
#                 pat += pattern_dict[char]
                
        
#         s_dict = {}
#         ss = ""
#         for char in s.split():
#             if char in s_dict:
#                 ss += s_dict[char]
#             else:
#                 s_dict[char] = str(len(s_dict)+1)
#                 ss += s_dict[char]
        
#         return pat == ss
            
        s, pattern = s.split(), list(pattern)
        return list(map(s.index, s)) == list(map(pattern.index, pattern))
