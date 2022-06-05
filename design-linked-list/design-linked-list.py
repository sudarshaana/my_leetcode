
class ListNode:
    def __init__(self, val, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev
        
class MyLinkedList:
    def __init__(self):
        self.sentinel_head = ListNode(0)
        self.sentinel_tail = ListNode(0)
        self.sentinel_head.next = self.sentinel_tail
        self.sentinel_tail.prev = self.sentinel_head
        self.size = 0
        
    def show(self):
        node = self.sentinel_head.next
        for _ in range(self.size):
            print(node.val, end=" ")
            node = node.next
        print()
            
        
    def addAtHead(self, value):
        new_head = ListNode(value, self.sentinel_head.next, self.sentinel_head)
        # updating old head ponters
        self.sentinel_head.next.prev = new_head
        self.sentinel_head.next = new_head
        self.size+=1
    
    def addAtTail(self, value):
        new_tail = ListNode(value, self.sentinel_tail, self.sentinel_tail.prev)
        self.sentinel_tail.prev.next = new_tail
        self.sentinel_tail.prev  = new_tail
        self.size+=1
        
    def addAtIndex(self, index, value):
        
        if index > self.size:
            return 

        if index < 0:
            index = 0
            
        # decide shortest node index position
        
        if index < self.size-index: # head is closer
            
            pred = self.sentinel_head
            for _ in range(index):
                pred = pred.next
                
            succ = pred.next                
            # adding node
            new_node = ListNode(value, succ, pred)
            pred.next = new_node
            succ.prev = new_node
            
        else: # tail is closer
            succ = self.sentinel_tail
            
            for _ in range(self.size-index):
                succ = succ.prev
                
            pred = succ.prev
            # new node
            new_node = ListNode(value, succ, pred)
            succ.prev = new_node
            pred.next = new_node
    
        self.size+=1
        
        
    def  deleteAtIndex(self, index):
        if index < 0 or index >= self.size:
            return
    
        # find predecessor and successor of the node to be deleted
        if index < self.size - index:
            pred = self.sentinel_head
            for _ in range(index):
                pred = pred.next
            succ = pred.next.next
        else:
            succ = self.sentinel_tail
            for _ in range(self.size - index - 1):
                succ = succ.prev
            pred = succ.prev.prev
        
        # delete pred.next 
        self.size -= 1
        pred.next = succ
        succ.prev = pred
        
        
    def get(self, index):
        # validating index
        if index < 0 or index > self.size-1:
            return -1
        
        if index < (self.size//2): # head
            node = self.sentinel_head
            for _ in range(index+1):
                node = node.next
                
            return node.val
        else:
            node = self.sentinel_tail
            for _ in range(self.size-index):
                node = node.prev
            return node.val
                
                
            