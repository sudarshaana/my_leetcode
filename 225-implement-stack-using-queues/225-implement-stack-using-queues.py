class MyStack:

    """
    Using Two Queue
    """
    
    def __init__(self):
        self.q1 = []
        self.q2 = []
        self.top_val = None

    def push(self, x: int) -> None:
        self.q1.append(x)
        self.top_val = x
        

    def pop(self) -> int:
        
        while len(self.q1) > 1:
            # pop element and add to q2
            item = self.q1.pop(0)
            self.top_val = item
            self.q2.append(item)
        # performing stack pop
        val = self.q1.pop()
        # copying q2 to q1
        self.q1 = self.q2.copy()
        self.q2 = []
        return val
            
    def top(self) -> int:
        return self.top_val

    def empty(self) -> bool:
        return len(self.q1) == 0
    
    
# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()