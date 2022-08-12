from collections import Counter
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        # s_col = Counter(stones)
        # s = set(jewels)
        # count = 0
        # for j in s:
        #     if j in s_col:
        #         count+= s_col[j]
        # return count
        
        j_set = set(jewels)
        count = 0
        for s in stones:
            if s in j_set:
                count+=1
                
        return count