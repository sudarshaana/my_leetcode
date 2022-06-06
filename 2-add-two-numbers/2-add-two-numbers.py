# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
#     def reverseLL(self, head):
#         prev = None
#         node = head
#         while node:
#             temp = node.next 
#             node.next = prev
#             prev = node
#             node = temp
#         return prev
    
#     def nodeToNumber(self, head):
#         number = 0
#         node = head
#         while node:
#             number = number*10 + node.val
#             node = node.next 
        
#         return number
    
#     def numberToNode(self, number):
        
#         head = ListNode(0)
#         node = head
#         if number == 0:
#             return head
        
#         while number!=0:
#             digit = number%10
#             new_node = ListNode(digit)
#             node.next = new_node
#             node = new_node
#             number = number// 10
            
#         return head.next
    
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode(0)
        node = dummy

        p1 = l1
        p2 = l2

        while p1 or p2:
            n1 = p1.val if p1 else 0
            n2 = p2.val if p2 else 0

            ans = n1+n2+carry
            carry = ans // 10
            node.next = ListNode(ans%10)
            node = node.next

            if p1:
                p1 = p1.next 
            if p2:
                p2 = p2.next 

        if carry > 0:
            node.next = ListNode(carry)


        return dummy.next
    
#         l1_rev = self.reverseLL(l1)
#         num1 = self.nodeToNumber(l1_rev)
        
#         l2_rev = self.reverseLL(l2)
#         num2 = self.nodeToNumber(l2_rev)
        
#         answer =  num1+num2 
#         return self.numberToNode(num1 + num2)
        