class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        prev_sum = 0
        rsum = sum(nums)
        
        for i, num in enumerate(nums):
            rsum -= num
            
            if prev_sum == rsum:
                return i
            
            prev_sum += num
        
        return -1