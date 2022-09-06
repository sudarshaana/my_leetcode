class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        nn = []
        for nums in matrix:
            nn+=nums
        nn = sorted(nn)
        return nn[k-1]