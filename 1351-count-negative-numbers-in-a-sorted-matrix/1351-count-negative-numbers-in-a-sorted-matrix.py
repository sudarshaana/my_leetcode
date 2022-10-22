class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        # brute force 
        
        count = 0
        for col in grid:
            for item in col:
                if item < 0:
                    count += 1
                    
        return count