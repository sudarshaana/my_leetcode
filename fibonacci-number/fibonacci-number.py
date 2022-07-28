class Solution:
    def __init__(self):
        self.visited = {}
        
    def fib(self, n, visited=None):
        if n in self.visited:
            return self.visited[n] 
        
        if n <= 0:
            return 0
        if n == 1:
            return 1
        
        self.visited[n] =  self.fib(n-1, self.visited)+self.fib(n-2, self.visited)
        return self.visited[n]