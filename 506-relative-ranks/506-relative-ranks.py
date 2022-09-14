class Solution:
    def findRelativeRanks(self, scores: List[int]) -> List[str]:
        
        heap = []
        for i, score in enumerate(scores):
             heapq.heappush(heap, (-score, i))
                
        
        medels = ["Gold Medal","Silver Medal","Bronze Medal"]
        i = 0
        ans = [None]*len(scores)
        
        while i < len(scores):
            val, pos = heapq.heappop(heap)
            if i < 3:                
                ans[pos] = medels[i]
            else:
                ans[pos] = str(i+1)
            i+=1
            
        return ans
        