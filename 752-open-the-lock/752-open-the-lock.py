class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
#         q = deque()
#         visited = set(deadends)
        
#         if '0000' in visited:
#             return -1
        
        
#         q.append(["0000", 0])
        
        
#         def combination(lock):
#             res = []
#             for i in range(4):
#                 num = str((int(lock[i])+1) % 10)
#                 comb = lock[:i] + num + lock[i+1:]
#                 res.append(comb)
                
#                 num = str((int(lock[i])-1 + 10) % 10)
#                 comb = lock[:i] + num + lock[i+1:]
#                 res.append(comb)
                
#             return res
                
        
        
        
#         while q:
#             lock, step = q.popleft()
            
#             if lock == target:
#                 return step
            
#             for child in combination(lock):
#                 if child not in visited:
#                     visited.add(child)
#                     q.append([child, step+1])
                    
    
#         return -1
        q = deque()
        visited = set(deadends)
        
        if '0000' in visited:
            return -1
        
        
        q.append(["0000", 0])
        
        
        def combination(lock):
            #res = []
            for i in range(4):
                for operation in (1, -1):
                    
                    num = str((int(lock[i])+ operation + 10) % 10)
                    comb = lock[:i] + num + lock[i+1:]
                    yield comb
            
        while q:
            lock, step = q.popleft()
            
            if lock == target:
                return step
            
            for child in combination(lock):
                if child not in visited:
                    visited.add(child)
                    q.append([child, step+1])
                    
    
        return -1