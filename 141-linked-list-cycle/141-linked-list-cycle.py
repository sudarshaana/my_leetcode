# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # using hasmap
        # hasmap = set()
        # node = head
        # while node is not None:
        #     if node not in hasmap:
        #         hasmap.add(node)
        #     else:
        #         return True
        #     node = node.next
        # return False
        
        # using two pointer
        
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next
            
            if fast == slow:
                return True
        return False