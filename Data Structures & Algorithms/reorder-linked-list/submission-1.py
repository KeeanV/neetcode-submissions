# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the middle
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # split into 2 lists
        second = slow.next
        slow.next = None

        # reverse the second half in place
        prev = None
        curr = second
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        second = prev

        # merge the alternating nodes
        first = head
        while second:
            lista = first.next
            listb = second.next
            first.next = second
            second.next = lista

            first = lista
            second = listb
        

