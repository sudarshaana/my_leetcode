class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        arr_l = len(arr)
        
        if arr_l == k:
            return arr
        
        
        left = self.search_closest(arr, x)
        #left = bisect_left(arr, x) - 1

        # print(left)
        # print("closest_position", closest_position, arr[closest_position])
        
        right = left + 1

        while right - left - 1 < k:
            if left == -1:
                right += 1
                continue
            
            if right == len(arr) or abs(arr[left] - x) <= abs(arr[right] - x):
                left -= 1
            else:
                right += 1
        
        # Return the window
        return arr[left + 1:right]
            
            
        
    
    def search_closest(self, nums, target):
        
        l, r = 0, len(nums)-1
        
        if nums[l] >= target:
            return l
        if nums[r] <= target:
            return r
        
        while l <= r:
            mid = l + (r-l)//2
            
            if nums[mid] == target:
                return mid
            if nums[mid] < target and nums[mid+1] > target:
                return mid if (target-nums[mid]) <= (nums[mid+1]-target) else mid+1
            elif nums[mid] < target:
                l = mid
            else:
                r = mid