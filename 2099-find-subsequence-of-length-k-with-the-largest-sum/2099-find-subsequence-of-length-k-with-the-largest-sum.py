class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        
        heap = []
        heapq.heapify(heap)
        
        for i, num in enumerate(nums):
            if len(heap) < k:
                heapq.heappush(heap, (num, i))
            else:
                heapq.heappushpop(heap, (num, i))
                
        #return heap
        heap.sort(key = lambda x: x[1])
        
        return [x[0] for x in heap]