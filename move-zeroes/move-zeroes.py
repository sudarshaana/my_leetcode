class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
#         zeros = 0
#         l = len(nums)
        
#         for i in range(l):
#             if nums[i] == 0:
#                 zeros+=1
#             else:
#                 nums[i-zeros] = nums[i]
                
#         while zeros!=0:
#             nums[l-zeros]=0
#             zeros-=1

        l = len(nums)
        i = 0
        while i<l:
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
                l-=1
            else:
                i+=1
                