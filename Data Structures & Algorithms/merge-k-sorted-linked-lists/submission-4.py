# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
      dummy = ListNode(0)
      curr = dummy
      my_heap = []

      for i, head in enumerate(lists):
        if head is not None:
            heapq.heappush(my_heap, (head.val, i, head))
      
      while my_heap:
        val, l, node = heapq.heappop(my_heap)
        curr.next = node
        curr = node
        if node.next:
            heapq.heappush(my_heap, (node.next.val, l, node.next))
      return dummy.next


