# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = self.nodeToNumber(l1)
        num2 = self.nodeToNumber(l2)

        answer =  num1+num2 
        return self.reverseLL(self.numberToNode(num1 + num2))

    
        
    def reverseLL(self, head):
        prev = None
        node = head
        while node:
            temp = node.next 
            node.next = prev
            prev = node
            node = temp
        return prev        
        
    
    def nodeToNumber(self, head):
        number = 0
        node = head
        while node:
            number = number*10 + node.val
            node = node.next 
        
        return number
    
    def numberToNode(self, number):
        
        head = ListNode(0)
        node = head
        if number == 0:
            return head
        
        while number!=0:
            digit = number%10
            new_node = ListNode(digit)
            node.next = new_node
            node = new_node
            number = number// 10
            
        return head.next
 
    