# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break

            groupNext = kth.next

            # reverse
            prev, curr = groupNext, groupPrev.next

            while curr!=groupNext:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            firstofK = groupPrev.next
            groupPrev.next = kth
            groupPrev = firstofK

        return dummy.next


    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k-=1
        return curr