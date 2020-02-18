class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def reverse(self, head, m, n):
        if not head:
            return

        dummy = Node(0)
        dummy.next = head
        p1 = dummy
        p2 = head

        for i in range(m-1):
            p1 = p1.next
            p2 = p2.next

        frozen_p1 = p1
        frozen_p2 = p2

        p1 = p1.next
        p2 = p2.next

        for j in range(n-m):
            p3 = p2.next
            p2.next = p1
            p1 = p2
            p2 = p3

        frozen_p1.next = p1
        frozen_p2.next = p2

        return dummy.next
