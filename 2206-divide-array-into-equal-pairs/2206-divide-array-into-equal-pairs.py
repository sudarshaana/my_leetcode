from collections import Counter
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        
#         c = Counter(nums)
        
#         for item in c.keys():
#             if c[item] % 2 != 0:
#                 return False
#         return True
        
        nset = set()
        
        for n in nums:
            if n in nset:
                nset.remove(n)
            else:
                nset.add(n)
        
        return len(nset) == 0