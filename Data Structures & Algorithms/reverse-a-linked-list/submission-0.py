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
        if not head:
            return None

        head_LL2 = ListNode(head.val)

        current = head
        while current.next is not None:
            new_head = ListNode(current.next.val)
            new_head.next = head_LL2
            head_LL2 = new_head
            current = current.next

        return head_LL2

