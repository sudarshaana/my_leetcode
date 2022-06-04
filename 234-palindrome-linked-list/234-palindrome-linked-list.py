# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def get_head_mid(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    
    def reverse_mid(self, head):
        prev = None
        current = head
        while current:
            temp = current.next 
            current.next = prev
            prev = current
            current = temp
            
        return prev
        
    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        head_first = head
        head_mid = self.get_head_mid(head)
        new_rev_head = self.reverse_mid(head_mid)
        
        head_last = new_rev_head
        
        while head_last:
            if head_first.val != head_last.val:
                return False
            head_first = head_first.next
            head_last = head_last.next 
            
        return True