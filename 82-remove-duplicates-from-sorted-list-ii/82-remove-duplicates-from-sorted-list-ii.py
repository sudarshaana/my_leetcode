# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head: # no element
            return head
        
        elif head.next == None: # 1 element
            return head
        
        elif head.next.next == None: # 2 elements
            if head.val == head.next.val:
                return None
            else:
                return head
        
        
        prev = head
        s_head = ListNode(0, prev)
        old = s_head
        node = prev.next
        delete = False
        
        while node:
            if prev.val == node.val:
                delete = True
                node = node.next
                
                if node == None:
                    old.next = None
                
            else:
                if delete:
                    old.next = node
                    prev = node
                    node = node.next
                    delete = False
                else:
                    old = prev
                    prev = node
                    node = node.next
                    
        return s_head.next
            