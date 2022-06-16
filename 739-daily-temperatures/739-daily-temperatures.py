class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        self.stack = []
        n = len(temperatures)
        self.ans = [0]*n
        
        for index, temp in enumerate(temperatures):
            
            while self.stack and temperatures[self.stack[-1]] < temp:
                pop_index = self.stack.pop()
                self.ans[pop_index] = index-pop_index
            self.stack.append(index)
            
        return self.ans