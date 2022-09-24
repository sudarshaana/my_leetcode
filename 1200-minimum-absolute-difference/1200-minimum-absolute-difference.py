class Solution:
    def minimumAbsDifference(self, nums: List[int]) -> List[List[int]]:
#         nums.sort()
        
#         diff_map = defaultdict(list)
        
#         for i, num in enumerate(nums[1:]):
#             diff = abs(num - nums[i])
#             diff_map[diff].append([nums[i], num] )
#         return diff_map[min(diff_map.keys())]

#         nums.sort()
        
#         min_diff = sys.maxsize
#         diff_map = []
        
#         for i, num in enumerate(nums[1:]):
#             diff = abs(num - nums[i])
            
#             if diff == min_diff:
#                 diff_map.append([nums[i], num])
                
#             elif diff < min_diff:
#                 min_diff = diff
#                 diff_map = [[nums[i], num]]
            
#         return diff_map

        # ---------------Using Count sort ----------------------
        mini, maxi = min(nums), max(nums)
        counter = [0] * (maxi-mini+1)
        shift = -mini
        
        for num in nums:
            counter[num+shift] = 1 
            
        min_abs_diff = maxi-mini
        min_abs_list = []
        
                
        prev = 0
        for curr in range(1, maxi+shift+1):
            
            if counter[curr] == 0:
                continue
            
            if curr-prev == min_abs_diff:
                min_abs_list.append([prev-shift, curr-shift])
                
            elif curr-prev < min_abs_diff:
                min_abs_list = [[prev-shift, curr-shift]]
                min_abs_diff = curr - prev
                
            prev = curr
            
        return min_abs_list