class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        visited = set()
        queue = deque()
        
        COLS = len(rooms[0])
        ROWS = len(rooms)
        
        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    queue.append([r,c])
                    visited.add((r, c))
                    
        def addRoom(r, c):
            if r < 0 or c < 0 or r == ROWS or c == COLS or (r, c) in visited or rooms[r][c] == -1:
                return
            
            visited.add((r, c))
            queue.append([r,c])
        
        dist = 0
        while queue:
            
            for q in range(len(queue)):
                r, c = queue.popleft()
                rooms[r][c] = dist
                addRoom(r+1, c)
                addRoom(r-1, c)
                addRoom(r, c+1)
                addRoom(r, c-1)
                
            dist+=1