"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        # if head is empty
        if not head:
            node = ListNode(insertVal)
            node.next = node
            return node
        
        
        prev = head
        current = head.next
        found_position =  False
        
        while True:
            if prev.val <= insertVal <= current.val:
                found_position = True
            
            elif prev.val > current.val:
                if prev.val <= insertVal or insertVal <= current.val:
                    found_position = True
            
            if found_position:
                prev.next = ListNode(insertVal, current)
                return head
            
            prev, current = current, current.next 
            
            if prev == head: 
                # position not found!
                prev.next = ListNode(insertVal, current)
                return head