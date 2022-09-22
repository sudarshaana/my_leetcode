# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = head
        
        def insert(dummy, nodex):
            node = ListNode(nodex.val)
            
            current = dummy
            while current.next:
                if node.val < current.next.val:
                    break
                current = current.next
                
            temp = current.next
            current.next = node
            node.next = temp
                    
        
        while curr:
            insert(dummy, curr)
            curr = curr.next
            
        node = dummy.next
        # while node:
        #     print(node.val, "-->", end=" ")
        #     node = node.next
        
        return dummy.next