class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        b1 = int(a, 2)
        b2 = int(b, 2)
        
        r = b1+b2
        return bin(r)[2:]