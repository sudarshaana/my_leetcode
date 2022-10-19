class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        if nums[0] < nums[-1]:
            return nums[0]
        
        left, right = 0, len(nums)-1
        
        while left < right:
            mid = (left+right)//2
            
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            
            elif nums[mid] > nums[0]:
                left = mid+1
            else:
                right = mid
        
        
        return nums[left]