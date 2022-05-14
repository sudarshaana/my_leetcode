class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        a, b, c = 0,0,0

        for i in range(len(cost)-1, -1, -1):
            a = cost[i] + min(b, c)
            c = b
            b = a

        return min(b, c)