class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        points = [( (x*x + y*y), [x,y] ) for x, y in points]
        
        points.sort()
        #print(points)
        
        return [y for x, y in points[:k] ]