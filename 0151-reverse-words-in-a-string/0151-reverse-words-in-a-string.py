class Solution:
    def reverseWords(self, s: str) -> str:
        
#         list_data = s.strip().split(" ")
#         list_data.reverse()
#         list_data = [s.strip() for s in list_data ]
        
#         list_data = list(filter(None, list_data))

        
#         #print(list_data)
        
#         return " ".join(list_data)
        
        return ' '.join(s.split()[::-1])
