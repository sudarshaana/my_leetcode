class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        heap = []#[(sum(row), i) for i, row in enumerate(mat)]
        
        # heapq.heapify(heap)
        # smallest = heapq.nsmallest(k, heap)
        # return [num[1] for num in smallest]
        
        heapq.heapify(heap)
        
        for i, row in enumerate(mat):
            
            heapq.heappush(heap, (-sum(row), -i))
            
            if len(heap) > k:
                heapq.heappop(heap)
                
        #print(heap)
        res = []
        while heap:
            res.append(-heapq.heappop(heap)[1])
            
        return res[::-1]
            