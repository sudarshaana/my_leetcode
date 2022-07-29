class Solution:
    from functools import lru_cache
    
    @lru_cache()
    def climbStairs(self, n: int) -> int:
        if n == 0 or n==1 or n==2:
            return n
        return self.climbStairs(n-1)+self.climbStairs(n-2)