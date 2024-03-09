class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        def dp(i):
            if i >= len(cost):
                return 0
            
            if i not in memo:
                one_step = cost[i]+dp(i+1)
                two_step = cost[i]+dp(i+2)
                min_cost = min(one_step, two_step)
                memo[i] = min_cost
                
            return memo[i]
        
        memo = {}
        return min(dp(0), dp(1))