class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        max_count = 0
        current_count = 0
        
        for num in nums:
            if num == 0:
                current_count = 0
            else:
                current_count+=1
                max_count = max(max_count, current_count)
                
        return max_count