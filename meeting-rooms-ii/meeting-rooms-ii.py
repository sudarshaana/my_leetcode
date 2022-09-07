class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        allocation = []
        intervals = sorted(intervals)
        allocation.append(intervals[0][1])
        #print(intervals)
        
        for intv in intervals[1:]:            
            
            inserted = False
            for i in range(len(allocation)):
                #print("allocation: --", allocation, "allow: ", allocation[i], "intv : ", intv)
                
                if allocation[i] <= intv[0]:
                    inserted = True
                    allocation[i] = intv[1]
                    break
            #print()
            if not inserted:
                allocation.append(intv[1])
                
        return len(allocation)