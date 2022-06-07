"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        # if head is empty
        if not head:
            node = ListNode(insertVal)
            node.next = node
            return node
        
        prev1 = head
        prev = head.next
        current = head.next.next
        
        while True:
            if prev.val > current.val:
                # smallest or largest
                
                #if the num is smallest
                if prev.val > insertVal and current.val >= insertVal:
                    new_node = ListNode(insertVal, current)
                    prev.next = new_node
                    break
                elif prev.val <= insertVal and current.val < insertVal: # the num is largest
                    new_node = ListNode(insertVal, current)
                    prev.next = new_node
                    break
                else:
                    prev1 = prev1
                    prev = current
                    current = current.next
                    
            elif prev.val < insertVal and current.val >= insertVal: # between
                new_node = ListNode(insertVal, current)
                prev.next = new_node
                break
            elif prev.val == current.val and prev1.val == prev.val:
                new_node = ListNode(insertVal, current)
                prev.next = new_node
                break
            # elif prev.val < insertVal and current.val <= insertVal:
            #     new_node = ListNode(insertVal, current)
            #     prev.next = new_node
            #     break
            else:
                prev1 = prev1
                prev = current
                current = current.next
            
        return head