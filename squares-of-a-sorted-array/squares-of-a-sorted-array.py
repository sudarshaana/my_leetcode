class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        num = len(nums)
        start = 0
        end = num-1
        
        sorted_list = [0]*num
        index = num-1
        
        
        while start<=end:
            if abs(nums[start]) > abs(nums[end]):
                sorted_list[index]=nums[start]**2
                start+=1
            else:
                sorted_list[index]=nums[end]**2
                end-=1
                
            index-=1
                
        return sorted_list