class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
#         start, end = -1,-1
        
#         for i in range(len(nums)):
#             if nums[i] ==  target:
#                 if start == -1:
#                     start = i
#                 end = i
            
#         return start, end

        start = self.find_left(nums, target)
        end = -1
        if start != -1:
            end = self.find_right(nums, start, target)
            
        return [start, end]
    

    def find_right(self, nums, l, target):
        r = len(nums)-1
        
        while l <= r:
            mid = l + (r-l)//2
            
            if nums[mid] == target:
                if mid == r or nums[mid+1] > target:
                    return mid
                else:
                    l = mid+1
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        
    def find_left(self, nums, target):
        
        l, r = 0, len(nums)-1
        
        while l <=r:
            mid = l + (r-l)//2
            
            if nums[mid] == target:
                if mid == l or nums[mid-1] < target:
                    return mid
                else:
                    r = mid - 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
                
        return -1