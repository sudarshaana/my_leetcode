class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        def get_min(nums):
            s = set(nums) 
            s = sorted(s)
            #min = sorted(s)[0] 
            min = s[0] if s[0] != 0 else s[1]
            return min
        
        step = 0
        
        while True:
            if nums[0] == 0 and (nums.count(nums[0]) == len(nums)):
                return step
            else:
                min = get_min(nums)
                nums = [value-min if value> 0 else value for value in nums ]
                step += 1