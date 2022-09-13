class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        used_ladder = []
        
        for i in range(len(heights)-1):
            diff = heights[i+1] - heights[i]
            
            if diff <= 0:
                #print(i, "diff", diff, i)
                continue

            #used_ladder.append(diff)
            heapq.heappush(used_ladder, diff)
            
            if ladders:
                #print(i, "ladder", diff, i)
                ladders -= 1
                continue

           # min_diff = min(used_ladder)
            bricks -= heapq.heappop(used_ladder)
            #used_ladder.remove(min_diff)
            
            # print("diff:", diff, "ladders:", ladders, "min_diff:", min_diff, "bricks", bricks, "used_ladder:",used_ladder, "i:", i)
            
            if bricks < 0:
                return i
        
        return len(heights)-1