# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        first = head
        for num in range(n):
            first = first.next
        
        dummy = ListNode()
        second = dummy
        second.next = head

        while first:
            first = first.next
            second = second.next

        nth = second.next
        print(nth.val)
        prev = second
        nxt = nth.next
        prev.next = nxt


        return dummy.next
        