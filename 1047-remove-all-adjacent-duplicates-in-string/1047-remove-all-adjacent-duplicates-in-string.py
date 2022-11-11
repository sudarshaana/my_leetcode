from string import ascii_lowercase
class Solution:
    def removeDuplicates(self, S: str) -> str:
#         new_s, removed = self.remove_adjacent_duplicate(s)

#         while removed:
#             new_s, removed = self.remove_adjacent_duplicate(new_s)
        
#         return new_s
    
#     def remove_adjacent_duplicate(self, s):
#         removed = False
#         for i, char in enumerate(s[:-1]):
#             if s[i] == s[i+1]:
#                 removed = True
#                 return s.replace(f"{char}{char}", ""), removed
#         return s, removed
        
#         duplicates = {2*ch for ch in ascii_lowercase}
        
#         prev_len = -1
#         while prev_len != len(S):
#             prev_len = len(S)
            
#             for d in duplicates:
#                 S = S.replace(d, "")
        
#         return S

        # using stack
        output = []
        
        for ch in S:
            if output and ch == output[-1]:
                output.pop()
            else:
                output.append(ch)
        
        return "".join(output)