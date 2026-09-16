# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    """
    find middle
    reverse second half
    pick 1 from first half, and bring end in the middle of first 2 
    nodes
    """
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half
        second = slow.next # slow has reached the middle
        prev = slow.next = None # first pointing to None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # merge 2 lists
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            second = tmp2
            first = tmp1

        
