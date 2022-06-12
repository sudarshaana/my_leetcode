# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head.next:
            return None
        
        s_head = ListNode(0, head)
        node = head
        slow, fast = node, node
        slow_prev = s_head
        
        while fast and fast.next:
            slow_prev = slow 
            slow = slow.next 
            fast = fast.next.next
            
            
        #print(slow_prev.val, slow.next.val)
        slow_prev.next = slow.next
    
        
        return head