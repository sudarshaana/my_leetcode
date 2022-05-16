class Solution:
    def rob(self, nums: List[int]) -> int:
        
    
        if len(nums) == 1:
            return nums[0]
    
        # bottomup table init
        dp = [0]*(len(nums))

        # initial base case
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
            #print(i)

        # returning last index of our table
        return dp[-1]