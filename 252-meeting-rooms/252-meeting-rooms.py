class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        allocation = []
        if len(intervals) <= 1:
            return True
        
        intervals = sorted(intervals)
        allocation.append(intervals[0][1])
        
        heapq.heapify(allocation)
        
        for intv in intervals[1:]:   
            
            if intv[0] < allocation[0]: 
                heapq.heappush(allocation, intv[1])
            else:
                heapq.heappushpop(allocation, intv[1])        
                
        return len(allocation) == 1