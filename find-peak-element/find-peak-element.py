class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
#         if len(nums) == 1:
#             return 0
        
#         for i in range(len(nums)-1):
#             if nums[i]>nums[i+1]:
#                 return i
            
#         return len(nums)-1

            
    
        # l = 0 
        # r = len(nums)-1
        # while (l<r):
        #     mid = l + (r-l)//2
        #     if nums[mid] > nums[mid+1]:
        #         r = mid
        #     else:
        #         l = mid+1
        # return l
        
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left+right)//2
            if nums[mid] < nums[mid+1]:
                left = mid + 1
            else:
                right = mid
        
        return left