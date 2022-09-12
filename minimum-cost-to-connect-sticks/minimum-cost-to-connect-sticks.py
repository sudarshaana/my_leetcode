class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        
        heapq.heapify(sticks)
        cost = 0
        
        while len(sticks) > 1:
            s1 = heapq.heappop(sticks)
            s2 = heapq.heappop(sticks)
            new_stick = s1+s2
            cost +=new_stick
            heapq.heappush(sticks, new_stick)            
            
        return cost