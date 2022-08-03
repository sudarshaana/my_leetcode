class Solution:
    def isHappy(self, n: int) -> bool:
        hashset = set()
        
        while n != 1:
            s = list(map(int, str(n)))
            n = 0
            for num in s:
                n += num*num
            if n in hashset:
                return False
            else:
                hashset.add(n)
        return True
