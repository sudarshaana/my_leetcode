# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return head
        
        node = head
        s_head = ListNode(-111, node)
        
        prev = s_head
        
        while node:
            if node.val == prev.val:
                # remove it
                prev.next = node.next
            else:
                prev = node
            node = node.next
            
        return s_head.next
        