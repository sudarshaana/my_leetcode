class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#         self.stack = []
#         n = len(temperatures)
#         self.ans = [0]*n
        
#         for index, temp in enumerate(temperatures):
            
#             while self.stack and temperatures[self.stack[-1]] < temp:
#                 pop_index = self.stack.pop()
#                 self.ans[pop_index] = index-pop_index
#             self.stack.append(index)
            
#         return self.ans
        n = len(temperatures)
        ans = [0] * n
        hottest = 0
        for index in range(n-1, -1, -1):
            current_temp = temperatures[index]
            if current_temp >= hottest:
                hottest = temperatures[index]
                continue
            
            
            day = 1
            while temperatures[day+index] <= current_temp:
                day += ans[day+index]
                
            ans[index] = day
        return ans