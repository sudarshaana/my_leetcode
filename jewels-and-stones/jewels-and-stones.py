from collections import Counter
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        s_col = Counter(stones)
        
        s = set(jewels)
        count = 0
        for j in s:
            if j in s_col:
                count+= s_col[j]
        return count