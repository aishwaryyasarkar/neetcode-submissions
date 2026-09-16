# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
    1->3->100
    2->102->200

    1->2->3->100->102

    as soon as a node greater than the one to add is visited, add to prev
"""
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # # if one of the list is empty
        # if not list1:
        #     return list2
        
        # if not list2:
        #     return list1

        # # use lowest head as base
        # if list1.val <= list2.val:
        #     start = list1
        # else:
        #     start = list2


        """
        1->3->100
        2->102->200

        1->2->3->100->102
        """
        dummy = ListNode()   # placeholder node, its job is just to give you a starting point
        tail = dummy         # tail always points to "the last node placed in the merged list"

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next

            

        
        