# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeRest(self, preNode, node):
                
        while node is not None:
            preNode.next = node
            preNode = preNode.next
            node = node.next 
        
    
    
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
        
        while node1 or node2:
            
            if not node1:
                self.mergeRest(prev, node2)
                break
            elif not node2:
                self.mergeRest(prev, node1)
                break
            elif node1.val < node2.val:                
                prev.next = node1
                prev = node1
                node1 = node1.next
            else:
                prev.next = node2
                prev = node2
                node2 = node2.next 
                
                
        return returnHead