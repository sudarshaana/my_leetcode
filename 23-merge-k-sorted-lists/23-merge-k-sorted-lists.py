# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from queue import PriorityQueue

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        class Wrapper():
            def __init__(self, node):
                self.node = node
            def __lt__(self, other):
                return self.node.val < other.node.val
            
        
        q = PriorityQueue()
        
        for l in lists:
            if l:
                q.put(Wrapper(l))
                
        senti = ListNode(0)
        head = senti
        while not q.empty():
            node = q.get().node
            head.next = node
            head = head.next
            if node.next:
                q.put(Wrapper(node.next))
        
        return senti.next
        
        
        
#         heap = []
#         heapq.heapify(heap)
        
#         for l in lists:
            
#             head = l
#             while head:
#                 heapq.heappush(heap, head.val)
#                 head = head.next
        
#         senti = ListNode(0)
#         head = senti
#         while heap:
#             head.next = ListNode(heapq.heappop(heap))
#             head = head.next
        
#         return senti.next