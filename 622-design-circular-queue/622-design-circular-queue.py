class ListNode:
    def __init__(self, x, next = None):
        self.val = x
        self.next = next
        
class MyCircularQueue:

#     def __init__(self, size):
#         self.size = size
#         self.list_size = 0
#         self.front = None
#         self.rear = None
        
        
        
#     def Front(self):
#         if self.list_size == 0:
#             return -1
#         else:
#             return self.front.val
    
#     def Rear(self):
#         if self.list_size == 0:
#             return -1
#         else:
#             return self.rear.val
            
            
#     def enQueue(self, val):
#         if self.list_size == self.size:
#             return False
#         else:
#             node = ListNode(val)
#             if self.rear == None:
#                 self.rear = node
#                 self.front = node
#             else:
#                 self.rear.next = node
#                 self.rear = node
#             self.list_size+=1
#             return True
            
#     def deQueue(self):
#         if self.list_size == 0:
#             return False
#         else:
#             self.front = self.front.next
#             self.list_size -= 1
#             if self.list_size == 0:
#                 self.front, self.rear = None, None
            
#             return True
        
    
#     def isEmpty(self):
#         return self.list_size == 0
    
#     def isFull(self):
#         return self.size == self.list_size

    
    def __init__(self, k: int):
        self.headIndex = 0
        self.capacity = k
        self.count = 0
        self.queue = [None]*k
        
    def enQueue(self, value: int) -> bool:
        if self.capacity == self.count:
            return False
        else:
            self.queue[(self.headIndex + self.count) % self.capacity] = value
            self.count +=1
            return True
            

    def deQueue(self) -> bool:
        if self.count == 0:
            return False
        else:
            self.headIndex = (self.headIndex+1) % self.capacity
            self.count -= 1
            return True
        
    def Front(self) -> int:
        if self.count == 0:
            return -1
        return self.queue[self.headIndex]

    def Rear(self) -> int:
        if self.count == 0:
            return -1
        return self.queue[(self.headIndex + self.count -1 ) % self.capacity]
        

    def isEmpty(self) -> bool:
        return self.count == 0
        

    def isFull(self) -> bool:
        return self.count == self.capacity
    



# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()