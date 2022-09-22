class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
#         for i in range(len(nums)):
#             min_index = i
            
#             for j in range(i+1, len(nums)):
#                 if nums[min_index] > nums[j]:
#                     min_index = j
            
#             nums[min_index], nums[i] =   nums[i] , nums[min_index]


        # using counting sort
        M = 2
        counter = [0]*(M+1)
        
        for item in nums:
            counter[item] += 1
                
        starting_index = 0
        for i, count in enumerate(counter):
            counter[i] = starting_index
            starting_index += count
                
        sorted_list = [0]*len(nums)
        for item in nums:
            sorted_list[counter[item]] = item
            counter[item]+=1
            
        for i in range(len(nums)):
            nums[i] = sorted_list[i]