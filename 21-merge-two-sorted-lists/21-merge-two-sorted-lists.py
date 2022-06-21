# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
#     def mergeTwoLists(self, headA: Optional[ListNode], headB: Optional[ListNode]) -> Optional[ListNode]:
#         # checking the input base case
#         if not headA:
#             return headB
#         elif not headB:
#             return headA
#         elif not headA and not headB:
#             return None
        
        
#         node1, node2, prev  = (headA, headB, headA) if headA.val < headB.val else (headB, headA, headB)
#         returnHead = prev
#         node1 = node1.next
        
#         while node1 and node2:
            
#             if node1.val < node2.val:                
#                 prev.next = node1
#                 prev = node1
#                 node1 = node1.next
#             else:
#                 prev.next = node2
#                 prev = node2
#                 node2 = node2.next 
                
#         if node1:
#             prev.next = node1
#         if node2:
#             prev.next = node2
            
#         return returnHead

    def mergeTwoLists(self, l1, l2):
        # maintain an unchanging reference to node ahead of the return node.
        prehead = ListNode(-1)

        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next            
            prev = prev.next

        # At least one of l1 and l2 can still have nodes at this point, so connect
        # the non-null list to the end of the merged list.
        prev.next = l1 if l1 is not None else l2

        return prehead.next