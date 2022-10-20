class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        #return min(nums)
        
#         left = 0
#         right = len(nums)-1
        

#         while left < right:

#             mid = (left + right)//2
            
#             if nums[right] < nums[mid]:
#                 left = mid+1
#             elif nums[right] > nums[mid]:
#                 right = mid
#             else:
#                 right -= 1
                    
                    
        
#         return nums[left]

        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
            elif nums[mid] <= nums[right]:
                right = mid
            else:
                left = mid + 1

        return nums[left]