class Solution:
    def fill(self, image, x, y, color, src_value):
        if image[x] [y] == src_value and image[x][y] != color:
            image[x] [y] = color
            self.queue.append([x,y])
            
    def __init__(self, *args, **kwargs):
        self.queue = []
        
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visited = set()
        
        if not image:
            return image
        ROW = len(image)
        COL = len(image[0])
        src_value = image[sr][sc]
        
        combinations = [
            [0, 0],
            [0, 1],
            [0,-1],
            [1, 0],
            [-1,0]
        ]
        self.queue.append([sr, sc])
        while self.queue:
            x, y = self.queue.pop()
            for delX, delY in combinations:
                r = x+delX
                c = y+delY
                
                if r < ROW and c < COL and c >=0 and r>=0 and (r, c) not in visited:
                    self.fill(image, r, c, color, src_value)
        return image