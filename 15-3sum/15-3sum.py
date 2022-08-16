class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        """ Using dic, no short """
        res, dups = set(), set()
        seen = {}
        
        for i, val1 in enumerate(nums):
            if val1 not in dups:
                dups.add(val1)
                for j, val2 in enumerate(nums[i+1:]):
                    complement = -val1 -val2
                    if complement in seen and seen[complement] == i:
                        res.add(tuple(sorted((val1, val2, complement))))
                    seen[val2] = i
        return res
        
        
#         ans = []
#         nums.sort()
        
#         for i in range(len(nums)):
#             if  nums[i]>0:
#                 break
#             if i == 0 or nums[i-1] != nums[i]:
#                 self.twoSum(i, nums, ans)
#         return ans
    
#     def twoSum(self, i, nums, res):
#         seen = set()
#         j = i+1
#         r = len(nums)
        
#         while j < r:
#             com = -nums[i] - nums[j]
            
#             if com in seen:
#                 res.append([nums[i], nums[j], com])
                
#                 while j + 1 < r and nums[j] == nums[j+1]:
#                     j+=1
#             seen.add(nums[j])
#             j+=1
            
        
#         target = -nums[i]
#         l = i+1
#         r = len(nums)-1
        
#         while l<r:
#             sum = nums[l]+nums[r]
            
#             if sum > target:
#                 r-=1
#             elif sum < target:
#                 l+=1
#             else:
#                 res.append( [-target, nums[l], nums[r] ])
#                 l+=1
#                 r-=1
#                 while l<r and nums[l]==nums[l-1]:
#                     l+=1