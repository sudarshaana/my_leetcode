# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        # we can use sentinel head , this will solve removing head issue
        sentinel_head = ListNode(0)
        sentinel_head.next = head
        
        prev = sentinel_head
        node = head
        
        while node is not None:
            if node.val == val:
                prev.next = node.next
            else:
                prev = node
            
            node = node.next
        
        
        return sentinel_head.next