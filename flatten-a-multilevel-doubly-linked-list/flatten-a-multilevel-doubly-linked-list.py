"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        self.merge(head)
        return head
    
    def merge(self, head):
        
        node = head
        while node:
            if node.child:
                next_node = node.next 
                child = node.child
                node.child = None
                # update nodes
                node.next = child
                child.prev = node
                
                tail = self.merge(child)
                
                if next_node:
                    tail.next = next_node
                    next_node.prev = tail
            
            if node.next is None:
                return node
            
            node = node.next