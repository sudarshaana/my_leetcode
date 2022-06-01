# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    
    def intersection(self, head):    
        fast = head
        slow = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next 

            if fast == slow:
                return slow
        return None
        
        
    def detectCycle(self, head) -> bool:
        
        if not head:
            return None
    
        cycle = self.intersection(head)
        if cycle is None:
            return None
        
        node1 = head
        node2 = cycle
        
        while node1 != node2:
            node1 = node1.next
            node2 = node2.next
            
        
        return node1