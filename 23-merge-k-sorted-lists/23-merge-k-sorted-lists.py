# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        heap = []
        heapq.heapify(heap)
        
        for l in lists:
            
            head = l
            while head:
                heapq.heappush(heap, head.val)
                head = head.next
        
        senti = ListNode(0)
        head = senti
        while heap:
            head.next = ListNode(heapq.heappop(heap))
            head = head.next
        
        return senti.next