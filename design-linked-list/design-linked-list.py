class Node:
    def __init__(self, value, next_node = None):
        self.next = next_node
        self.value = value
        

class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        count = 0
        if self.head is None:
            return -1
        
        next_node = self.head
        while next_node:
            if count == index:
                return next_node.value
            next_node = next_node.next
            count+=1
            
        return -1
        

    def addAtHead(self, val: int) -> None:
        if self.head is not None:
            node = Node(val, self.head)
        else:
            node = Node(val, None)
        self.head = node
            

    def addAtTail(self, val: int) -> None:
        if self.head is None:
            self.addAtHead(val)
            return
        
        next_node = self.head
        while next_node is not None:
            if next_node.next is None:
                tail_node = Node(val, None)
                next_node.next = tail_node
                break
            next_node = next_node.next
                

    def addAtIndex(self, index: int, val: int) -> None:
        
        if index == 0:
            self.addAtHead(val)
            return
        
        count = 0
        current_node = self.head
        prev_node = self.head
        
        while current_node is not None:
            # if index == 0, insert it as head
            if index == 0:
                self.addAtHead(val)
                break

            elif count == index:
                #print(str(next_node.value), "added")
                new_node = Node(val, current_node)
                prev_node.next = new_node
                #current_node.next = next_node
                break
            
            elif current_node.next is None:
                # checking if it is tail
                self.addAtTail(val)
                break
                
            prev_node = current_node
            current_node = current_node.next
            
            count+=1
            
    def deleteAtIndex(self, index: int) -> None:
        node = self.head
        if index == 0:
            # delete head
            self.head = self.head.next
            return
        
        prev_node = self.head
        count = 0
        while node is not None:
            if count == index:
                prev_node.next = node.next
            prev_node = node
            node = node.next
            count+=1
            
    def show(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next
            