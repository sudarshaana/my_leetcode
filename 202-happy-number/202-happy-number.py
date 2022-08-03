class Solution:
    def isHappy(self, n: int) -> bool:
        hashset = set()
        
        while n != 1:
#             s = list(map(int, str(n)))
#             n = 0
#             for num in s:
#                 n += num*num
             
            total = 0
            while n//10 != 0:
                total += (n%10)**2
                n = n// 10
            n = n*n + total

            if n in hashset:
                return False
            else:
                hashset.add(n)
        return True
