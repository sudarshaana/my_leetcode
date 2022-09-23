class Solution:
    def minimumAbsDifference(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        diff_map = defaultdict(list)
        
        for i, num in enumerate(nums[1:]):
            diff = abs(num - nums[i])
            diff_map[diff].append([nums[i], num] )
        return diff_map[min(diff_map.keys())]