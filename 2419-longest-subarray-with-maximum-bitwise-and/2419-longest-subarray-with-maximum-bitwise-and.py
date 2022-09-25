class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
#         count = 1
#         max_num = nums[0] 
#         mm = 1
#         sub_array = True

#         for i, num in enumerate(nums[1:]):
            
#             if num == max_num and sub_array:
#                 count+=1
#                 mm = max(count, mm)
#                 #sub_array = False
#                 #print(count)
            
#             elif num >= max_num:
#                 if num > max_num:
#                     mm = 1
#                 max_num = num
#                 sub_array = True
#                 count = 1
                
#             else:
#                 sub_array = False
        
#         return mm
        
        max_num = max(nums)
        max_count = 0
        for x, y in groupby(nums):
            if x == max_num:
                max_count = max(max_count, len(list(y)))
        return max_count