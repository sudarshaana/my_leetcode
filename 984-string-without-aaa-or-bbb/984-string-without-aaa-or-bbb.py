class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        ans = []
        
        while a or b:
            if len(ans)>=2 and ans[-1] == ans[-2]:
                writeA = ans[-1]=='b'
            else:
                writeA = a>b
            
            if writeA:
                ans.append('a')
                a-=1
            else:
                ans.append('b')
                b-=1
                
        return ''.join(ans)
        
        
        #s = []
#         if a==b:
#             while a!=0 and b!=0:
#                 s.append('a')
#                 s.append('b')
#                 a-=1
#                 b-=1
        
#         largerA = True if a>b else False        
        
#         while a!=0 and b!=0:
#             if a == b:
#                 if largerA:
#                     s.append('a')
#                     s.append('b')
#                 else:
#                     s.append('b')
#                     s.append('a')
#             else:
#                 if largerA:
#                     s.append('aa')
#                     s.append('b')
#                     a-=1
#                 else:
#                     s.append('bb')
#                     s.append('a')
#                     b-=1
#             a-=1
#             b-=1
#         if a!=0:
#             s.append('a'*a)
#         if b!=0:
#             s.append('b'*b)
            
#         return ''.join(s)
        