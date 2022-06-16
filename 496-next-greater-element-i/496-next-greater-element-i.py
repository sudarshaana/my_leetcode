from collections import defaultdict

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        self.hash = defaultdict(lambda:-1)
        self.stack = []
        
        for index, num in enumerate(nums2):
            
            while self.stack and nums2[self.stack[-1]] < num:
                pop_index = self.stack.pop()
                self.hash[nums2[pop_index]] = num
            self.stack.append(index)
            
        res = []
        for num in nums1:
            res.append(self.hash[num])
        return res