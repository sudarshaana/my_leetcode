
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        # using sort
        
        nums.sort()
        prev = nums[0]
        for num in nums[1:]:
            if prev == num:
                return num
            prev = num
        
        
        # using set
        # s = set()
        # for num in nums:
        #     if num in s:
        #         return num
        #     else:
        #         s.add(num)
        
        
        # using Binary search
        
#         # 'low' and 'high' represent the range of values of the target
#         low = 1
#         high = len(nums) - 1
        
#         while low <= high:
#             cur = (low + high) // 2
#             count = 0

#             # Count how many numbers are less than or equal to 'cur'
#             count = sum(num <= cur for num in nums)
            
#             if count > cur:
#                 duplicate = cur
#                 high = cur - 1
#             else:
#                 low = cur + 1
                
#         return duplicate