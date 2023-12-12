class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_num =max(nums)        
        index = nums.index(max_num)
        nums.remove(max_num)
        if max_num >= max(nums)*2:
            return index

        return -1

#         # another approach: find max & 2nd max, them check if max >= 2*end Max
    
#         f_max = nums[0]
#         s_max = None
#         max_index = 0
        
#         for i, num in enumerate(nums[1:]):
#             if num > f_max:
#                 s_max = f_max
#                 f_max = num
#                 max_index = i+1
#             elif not s_max or num > s_max:
#                 s_max = num
        
#         # print(f_max, s_max, max_index)
        
#         return max_index if f_max >= 2*s_max else -1
        