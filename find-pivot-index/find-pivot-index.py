class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        prev_sum = 0
        
        for i, num in enumerate(nums):
            if prev_sum == sum(nums[i+1:]):
                return i
            
            prev_sum = sum(nums[:i+1])
        
        return -1