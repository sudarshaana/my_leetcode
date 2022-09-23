class Solution:
    def minimumAbsDifference(self, nums: List[int]) -> List[List[int]]:
#         nums.sort()
        
#         diff_map = defaultdict(list)
        
#         for i, num in enumerate(nums[1:]):
#             diff = abs(num - nums[i])
#             diff_map[diff].append([nums[i], num] )
#         return diff_map[min(diff_map.keys())]

        nums.sort()
        
        min_diff = sys.maxsize
        diff_map = []
        
        for i, num in enumerate(nums[1:]):
            diff = abs(num - nums[i])
            
            if diff == min_diff:
                diff_map.append([nums[i], num])
                
            elif diff < min_diff:
                min_diff = diff
                diff_map = [[nums[i], num]]
            
        return diff_map