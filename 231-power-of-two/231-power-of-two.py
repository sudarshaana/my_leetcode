class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return False
            
        l = math.log2(n)
        #print(l, int(l), l == int(l))
        return l == int(l)