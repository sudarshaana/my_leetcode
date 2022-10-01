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

    def binary_search(self, nums, target, left, right):

        while left <= right:

            mid = left + (right-left)//2
            if nums[mid] ==  target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1       
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 1:
            return 0 if nums[0] == target else -1
        
        ins_point = self.intersection(nums, 0, n-1)
        
        if target == nums[0]:
            return 0

        if ins_point == 0:
            return self.binary_search(nums, target, 0, n-1 )
        elif target > nums[0]:
            return self.binary_search(nums, target, 0, ins_point)
        else:
            return self.binary_search(nums, target, ins_point, n-1)
