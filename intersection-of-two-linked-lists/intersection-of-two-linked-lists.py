# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
#         hashset = set()
#         nodeA = headA
#         nodeB = headB
        
#         while nodeA or nodeB:
        
#             if nodeA is not None:
#                 if nodeA in hashset:
#                     return nodeA
#                 hashset.add(nodeA)
            
#             if nodeB is not None:
#                 if nodeB in hashset:
#                     return nodeB
#                 hashset.add(nodeB)
            
#             if nodeA is not None:
#                 nodeA = nodeA.next
#             if nodeB is not None:
#                 nodeB = nodeB.next
                        
#         return None
        hashset =set()
        node = headA
        while node:
            hashset.add(node)
            node = node.next
            
        node = headB
        while node:
            if node in hashset:
                return node
            node = node.next
        return None