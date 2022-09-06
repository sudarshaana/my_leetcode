class Solution:
    
#     def binary_search(self, data):
#         low = 0
#         high = len(data)
        
#         while low < high:
#             mid = low + (high-low)//2
#             if data[mid] == 1:
#                 low = mid + 1
#             else:
#                 high = mid
            
#         return low
    
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        heap = []#[(sum(row), i) for i, row in enumerate(mat)]
        
        # heapq.heapify(heap)
        # smallest = heapq.nsmallest(k, heap)
        # return [num[1] for num in smallest]
        
#         heapq.heapify(heap)
        
#         for i, row in enumerate(mat):
            
#             heapq.heappush(heap, (-self.binary_search(row), -i))
            
#             if len(heap) > k:
#                 heapq.heappop(heap)
                
#         #print(heap)
#         res = []
#         while heap:
#             res.append(-heapq.heappop(heap)[1])
            
#         return res[::-1]
        
        m, n = len(mat), len(mat[0])
        indexes = []
        
        for c, r in product(range(n), range(m)):
            if len(indexes) == k:
                break
            if mat[r][c] == 0 and (c == 0 or mat[r][c-1] == 1):
                indexes.append(r)
                
                
        i = 0
        while len(indexes) < k:

            if mat[i][-1] == 1:
                indexes.append(i)
            i+=1
                    
        return indexes
        