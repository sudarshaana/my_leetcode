# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def get_size(self, head):
        size = 1;
        node = head
        while node:
            if node.next == None:
                node.next = head
                break
            node = node.next
            size+=1
        return size
    
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0:
            return head
        
        if not head:
            return head
        elif not head.next:
            return head
        size = self.get_size(head)
        target_pos = size - (k % size)-1
        
        
        node = head
        for i in range(target_pos):
            node = node.next
            
        new_head = node.next
        node.next = None
    
        return new_head