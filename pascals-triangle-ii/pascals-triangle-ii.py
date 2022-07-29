class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        
        # def value(i, j, memory=None):
        #     if (i,j) in memory:
        #         return memory[(i,j)]
        #     if i == j or j == 0:
        #         return 1
        #     memory[(i,j)] = value(i-1, j-1, memory) + value(i-1, j, memory)
        #     return memory[(i,j)]
        # memory = {}
        # l = []
        # for i in range(rowIndex+1):
        #     l.append(value(rowIndex, i, memory))
        # return l
        
        from functools import lru_cache
        @lru_cache()
        def value(i, j):
            if i == j or j == 0:
                return 1
            return value(i-1, j-1) + value(i-1, j)
        
        l = []
        for i in range(rowIndex+1):
            l.append(value(rowIndex, i))
        return l