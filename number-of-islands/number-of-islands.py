class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
#         q = deque()
        
#         ROWS = len(grid)
#         COLS = len(grid[0])
        
#         self.island_count = 0
        
        
#         def checkNeigbour(r, c):
#             if r < 0 or c < 0 or r == ROWS or c == COLS or grid[r][c] == '0':
#                   return
#             q.append([r,c])
#             grid[r][c] = '0'
#             #visited.add((r,c))
        
#         def countIsland(r, c):
#             q.append([r,c])
#             self.island_count+=1
            
#             while q:
#               r, c = q.popleft() # using queue
#               grid[r][c] = '0'
              
#               checkNeigbour(r+1, c)
#               checkNeigbour(r-1, c)
#               checkNeigbour(r, c+1)
#               checkNeigbour(r, c-1)
                  
            
        
#         for r in range(ROWS):
#             for c in range(COLS):
#                 if grid[r][c] == '0':
#                   continue
#                 countIsland(r, c)
                
#         return self.island_count

        q = deque()
        
        ROWS = len(grid)
        COLS = len(grid[0])
        
        self.island_count = 0
        
        
        def checkNeigbour(r, c):
            if r < 0 or c < 0 or r == ROWS or c == COLS or grid[r][c] == '0':
                  return
            q.append([r,c])
            grid[r][c] = '0'
            #visited.add((r,c))
        
        def countIsland(r, c):
            q.append([r,c])
            self.island_count+=1
            
            while q:
              r, c = q.pop() # using stack
              grid[r][c] = '0'
              
              checkNeigbour(r+1, c)
              checkNeigbour(r-1, c)
              checkNeigbour(r, c+1)
              checkNeigbour(r, c-1)
                  
            
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '0':
                  continue
                countIsland(r, c)
                
        return self.island_count