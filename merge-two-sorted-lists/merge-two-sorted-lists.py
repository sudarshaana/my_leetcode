# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def mergeTwoLists(self, headA: Optional[ListNode], headB: Optional[ListNode]) -> Optional[ListNode]:
        # checking the input base case
        if not headA:
            return headB
        elif not headB:
            return headA
        elif not headA and not headB:
            return None
        
        
        node1, node2, prev  = (headA, headB, headA) if headA.val < headB.val else (headB, headA, headB)
        returnHead = prev
        node1 = node1.next
        
        while node1 and node2:
            
            if node1.val < node2.val:                
                prev.next = node1
                prev = node1
                node1 = node1.next
            else:
                prev.next = node2
                prev = node2
                node2 = node2.next 
                
        if node1:
            prev.next = node1
        if node2:
            prev.next = node2
            
        return returnHead