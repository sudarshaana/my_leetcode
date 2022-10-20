class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        #return min(nums)
        
        if len(nums) == 1:
            return nums[0]
        
        if nums[0] < nums[-1]:
            return nums[0]
        
        
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