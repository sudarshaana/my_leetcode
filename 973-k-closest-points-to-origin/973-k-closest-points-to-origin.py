class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        #points = [( (x*x + y*y), [x,y] ) for x, y in points]
        
        points.sort(key = lambda p : p[0]**2 + p[1]**2)
        #print(points)
        
        return points[:k] #[y for x, y in points[:k] ]
        
        