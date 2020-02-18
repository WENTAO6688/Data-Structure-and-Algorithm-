'''
Reverse a linked list.

Input: 1->2->3->null
Output: 3->2->1->null

Input: 1->2->3->4->null
Output: 4->3->2->1->null
'''
class Solution:

    def reverse(self, head):
        if not head or not head.next:
            return head

        prev = None
        cur = head

        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next

        return prev
