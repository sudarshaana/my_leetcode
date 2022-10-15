class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        
#         appears = []
        
#         for item in arr1:
#             if self.search(arr2, item):
#                 appears.append(item)
                
#         app = []
#         for item in appears:            
#             if self.search(arr3, item):
#                 app.append(item)
        
        
#         return app


            s1 = set(arr1)
            s2 = set(arr2)
            s3 = set(arr3)
            
            return sorted((s1.intersection(s2)).intersection(s3))
    
#     def search(self, nums, target):
#         l, r = 0, len(nums)-1
        
#         while l <= r:
#             mid = l + (r-l)//2
            
#             if nums[mid] == target:
#                 return True
            
#             elif nums[mid] > target:
#                 r = mid - 1
#             else:
#                 l = mid + 1
        
#         return False