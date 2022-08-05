# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head, left, right): 
        prev = None
        current = head 
        
        while left <= right:
            temp = current.next
            current.next = prev 
            prev = current 
            current = temp 
            left+=1
        
        return prev, head, current
    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if k == 1 or not head:
            return head
        
        s_head = ListNode(0, head)
        
        current = s_head
        left, right = 1, 0
        
        while current.next:
            node = current
            
            for j in range(k):
                node = node.next
                if not node:
                    break
                right += 1
                
            if right % k == 0:
                new_head, new_tail, tail_next = self.reverse(current.next, left, right)
                current.next = new_head
                new_tail.next = tail_next
                current = new_tail
                left+=k
                
            else:
                break
                
        
        
        return s_head.next