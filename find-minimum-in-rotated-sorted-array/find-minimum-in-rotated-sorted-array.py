class Solution:
    def intersection(self, nums, left, right):
        if nums[right] > nums[left]:
            return 0

        while left <= right:
            mid = left + (right-left)//2

            if nums[mid] > nums[mid+1]:
                 return mid + 1
            else:
                if nums[mid] < nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1
                    
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return nums[self.intersection(nums, 0, len(nums)-1)]