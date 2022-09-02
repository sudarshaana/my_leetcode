class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        nums = [x*-1 for x in nums]
        heapq.heapify(nums)
        
        
        
        for i in range(len(nums)):
            num = nums[0]
            heapq.heappop(nums)
            
            if i == k-1:
                return -num