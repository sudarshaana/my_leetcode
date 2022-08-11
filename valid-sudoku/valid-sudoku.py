class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for rows in board:
            h = set()
            for value in rows:
                if value != ".":
                    
                    if value in h:
                        #print("1")
                        return False
                    else:
                        h.add(value)           
            
            
        
        for start in [0,3,6]:
            for end in [0,3,6]:
                x = set()
                for i in range(start, start+3):
                    for j in range(end, end+3):
                        if board[i][j] != ".":
                            
                            if board[i][j] in x:
                                return False
                            else:
                                x.add(board[i][j])
                        
            
            
        for i in range(9):
            h = set()
            for j in range(9):
                if board[j][i] != ".":
                    if board[j][i] in h:
                        return False
                    else:
                        h.add(board[j][i])    
                    
        return True