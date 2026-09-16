# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    """
        [(0,1),(1,2),(2,3),(3,None)]
        [(1,0),(0,None)]
    """
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prev = None
        while current is not None:
            _next = current.next
            current.next = prev
            prev = current
            current = _next

        return prev

