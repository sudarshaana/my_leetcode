# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        node = head
        while node:
            size+=1
            node = node.next
        
        node = head
        target_node_position = size - n 
        
        # head
        if target_node_position == 0:
            return head.next
        
        target_node_position -=1
       
        # head is removed, now the rest of them
        for i in range(target_node_position+1):
            if i == target_node_position:
                node.next = node.next.next
            node = node.next
                
        return head 
                