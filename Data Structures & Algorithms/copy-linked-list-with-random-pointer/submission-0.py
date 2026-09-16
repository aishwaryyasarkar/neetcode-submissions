"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashMap = {}

        curr = head
        while curr:
            newNode = Node(curr.val)
            hashMap[curr]=newNode
            curr = curr.next

        curr = head
        dummy = Node(0)
        tail = dummy

        while curr:
            if curr.next:
                nxt_copy = hashMap[curr.next]
            else:
                nxt_copy = None
            curr_copy = hashMap[curr]
            if curr.random:
                random_copy = hashMap[curr.random]
            else:
                random_copy = None
            curr_copy.next = nxt_copy
            curr_copy.random = random_copy
            tail.next = curr_copy
            tail = tail.next
            curr = curr.next

        return dummy.next

