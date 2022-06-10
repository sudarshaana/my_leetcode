"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def __init__(self):
        self.hashset = {}
        
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_node = head
        new_head = self.get_new_node(old_node)
        new_node = new_head
        
        while old_node:
            old_next = old_node.next 
            new_next = self.get_new_node(old_next)
            new_node.next = new_next
            
            old_random = old_node.random
            new_random = self.get_new_node(old_random)
            new_node.random = new_random
            
            old_node = old_node.next 
            new_node = new_node.next
            
        return new_head
    

    def get_new_node(self, old_node):
        if not old_node:
            return None
        
        if old_node not in self.hashset:
            # create a new one
            new_node = Node(old_node.val)
            self.hashset[old_node] = new_node
        return self.hashset[old_node]
        
        
        