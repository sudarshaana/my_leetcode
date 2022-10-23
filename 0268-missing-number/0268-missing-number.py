class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        # s = set(nums)
        # for n in range(len(nums)+1):
        #     if n not in s:
        #         return n
        
        
        nums.sort()
        for i in range(len(nums)):
            if i != nums[i]:
                return i
            
        return len(nums)