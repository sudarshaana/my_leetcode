class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        #return min(nums)
        
        left = 0
        right = len(nums)-1
        

        while left < right:

            mid = (left + right)//2
            
            if nums[right] < nums[mid]:
                left = mid+1
            elif nums[right] > nums[mid]:
                right = mid
            else:
                right -= 1
                    
                    
        
        return nums[left]