class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def remove_Nth_node(self, head, n):
        dummy = Node(0)
        cur = dummy
        prev = dummy
        node = head
        cur.next = head
        count = 0

        while cur.next is not None:
            cur = cur.next
            count += 1

        for i in range(count-n):
            node = node.next
            prev = prev.next

        deleted_node = node

        prev.next = deleted_node.next

        return dummy.next
