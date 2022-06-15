# class ListNode:
#     def __init__(self, x, min = None):
#         self.val = x
#         self.next = None
#         self.min = min
        
class MinStack:

#     def __init__(self):
#         self.head = None
#         self.min = None
        

#     def push(self, value: int) -> None:
#         if not self.head:
#             self.head = ListNode(value, value)
#             self.min = value
#         else:
#             min = value if value < self.min else self.min
#             self.min = min
#             node = ListNode(value,  min)
#             node.next = self.head
#             #self.head.next = node
#             self.head = node

#     def pop(self) -> None:
#         if self.head is not None:
#             self.head = self.head.next
#             if self.head is not None:
#                 self.min = self.head.min
#             else:
#                 self.min = None

#     def top(self) -> int:
#         if self.head is not None:
#             return self.head.val
        

#     def getMin(self) -> int:
#         return self.min
    def __init__(self):
        self.stack = []
        
    def push(self, value):
        if not self.stack: # empty stack
            self.stack.append([value, value])
        else:
            minimum = value if value < self.getMin() else self.getMin()
            self.stack.append( [value, minimum] )
            
    def getMin(self):
        #print(self.stack)
        return self.stack[-1][1]
    
    def pop(self):
        self.stack.pop()
            
    def top(self):
        if self.stack is not None:
            return self.stack[-1][0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()