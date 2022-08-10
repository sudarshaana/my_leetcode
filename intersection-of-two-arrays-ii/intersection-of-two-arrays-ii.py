from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        
        ans = []
        
        for val in c1.keys():
            if val in c2:
                ans+= [val] * min(c1[val], c2[val])
                
        return ans