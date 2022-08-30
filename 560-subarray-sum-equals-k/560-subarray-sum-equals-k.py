class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        count = 0
        total = 0
        
        d = {}
        d[0] = 1
        
        for num in nums:
            total += num
            
            if total-k in d:
                count += d[total-k]
            d[total] = d.get(total, 0) +1
            
        return count