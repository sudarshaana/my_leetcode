class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        heap = [(sum(row), i) for i, row in enumerate(mat)]
        
        heapq.heapify(heap)
        smallest = heapq.nsmallest(k, heap)
        return [num[1] for num in smallest]