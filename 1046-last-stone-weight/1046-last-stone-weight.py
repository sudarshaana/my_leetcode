class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones = [-x for x in stones]
        heapq.heapify(stones)
        
        while len(stones)>1:
            #print(stones)
            y = -heapq.heappop(stones)
            x = -heapq.heappop(stones)
            #print(y, x)
            
            if x!=y:
                heapq.heappush(stones, -(y-x))
        
        if len(stones) == 0:
            return 0
        return -stones[0]