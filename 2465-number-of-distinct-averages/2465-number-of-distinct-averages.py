class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        
        avg = set()
        
#         while nums:
#             maxi, mini = max(nums), min(nums)
#             nums.remove(maxi)
#             nums.remove(mini)
#             avg.add((maxi+mini)/2)
            
#         return len(avg)
        
        nums.sort()
        while nums:
            maxi, mini = nums[-1], nums[0]
            nums.pop(0)
            nums.pop(-1)
            avg.add((maxi+mini)/2)
            
        return len(avg)