class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        self.stack = []
    
        for i, price in enumerate(prices):
            
            while self.stack and prices[self.stack[-1]] >= price:
                indexPoped = self.stack.pop()
                prices[indexPoped] -= price
                    
            self.stack.append(i)
        
        return prices