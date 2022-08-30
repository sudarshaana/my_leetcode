class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        count = 0
        total = 0
        
        d = {0:1}
        
        for num in nums:
            total += num
            
            if total-k in d:
                count += d[total-k]
            if total in d:
                d[total] += 1
            else:
                d[total] = 1
            
        return count