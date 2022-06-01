# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # hashset = set()
        # nodeA = headA
        # nodeB = headB
        
        # while nodeA or nodeB:
        
        #     if nodeA is not None:
        #         if nodeA in hashset:
        #             return nodeA
        #         hashset.add(nodeA)
            
        #     if nodeB is not None:
        #         if nodeB in hashset:
        #             return nodeB
        #         hashset.add(nodeB)
            
        #     if nodeA is not None:
        #         nodeA = nodeA.next
        #     if nodeB is not None:
        #         nodeB = nodeB.next
                        
        # return None
        
        # hashset =set()
        # node = headA
        # while node:
        #     hashset.add(node)
        #     node = node.next
            
        # node = headB
        # while node:
        #     if node in hashset:
        #         return node
        #     node = node.next
        # return None
        
        # with two pointer technique
        # method:
        # if la == lb, no problem, we'll just get it
        # different: d = abs(a-b), when one pointer  hit null, and the other p2 position, then if we point the short pointer to the head of longer node
        # that will be ahead of the longer node with d distance
        # then when the longer node pointer hit null, we'll point to the shorter head, at this time our short pointer is alredy passed d distance
        # which is the difference;
        # now the will move keeping the pace, and intersect with their meeting point.
        
            
        nodeA = headA
        nodeB = headB
        
        while nodeA != nodeB:
            nodeA = headB if nodeA is None else nodeA.next
            nodeB = headA if nodeB is None else nodeB.next
            
        return nodeA