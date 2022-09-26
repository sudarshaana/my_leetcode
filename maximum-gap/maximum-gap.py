class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        
        if len(nums) < 2:
            return 0
        
        nums.sort()
        max_dis = 0
        
        
        for i in range(len(nums)-1):
            max_dis = max(max_dis, nums[i+1] - nums[i])
        return max_dis