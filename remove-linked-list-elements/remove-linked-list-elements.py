# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        prev = head
        node = head
        
        while node is not None:
            if node.val == val:
                if node is head:
                    head = head.next
                    prev = head
                else:
                    prev.next = node.next
            else:
                prev = node
            
            node = node.next
        
        
        return head