from collections import Counter
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        
        c = Counter(nums)
        
        for item in c.keys():
            if c[item] % 2 != 0:
                return False
        return True