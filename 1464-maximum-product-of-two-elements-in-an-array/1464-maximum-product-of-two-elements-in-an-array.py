class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        nums = [-num for num in nums]
        
        heapq.heapify(nums)
        #print(nums)
        return(heapq.heappop(nums) +1) * (heapq.heappop(nums)+1)
        #return (nums[0]+1)*(nums[1]+1)
        
#         n1 = nums[0]
#         n2 = nums[1]
        
#         for num in nums[2:]:
#             if num > n1:
#                 if n1>n2:
#                     n2=n1
#                 n1 = num
                 
#             elif num > n2:
#                 n2 = num
#                 if n2>n1:
#                     n1=n2
                
#         #print(n1, n2)
        
#         return (n1-1)*(n2-1)