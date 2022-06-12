# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotate_last(self, head):
        node = head
        prev = None
        while node:
            temp = node.next 
            node.next = prev
            prev = node
            node = temp
            
        #self.show(prev)
        return prev
    
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        node = head
        slow, fast = node, node
        
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next
            
        end_head = self.rotate_last(slow.next)
        slow.next = None
        
        start = head
        
        while start and end_head:
            start_next = start.next 
            end_next = end_head.next 
            start.next = end_head
            end_head.next = start_next
            
            start = start_next
            end_head = end_next
        
        return head
        