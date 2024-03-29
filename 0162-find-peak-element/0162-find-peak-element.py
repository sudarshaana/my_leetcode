class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return 0
        
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                return i
            
        return len(nums)-1