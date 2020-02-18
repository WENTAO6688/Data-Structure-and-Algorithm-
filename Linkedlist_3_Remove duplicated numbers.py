'''
Given a sorted linked list, delete all duplicates such that each element appear only once.

Input: null
Output: null

Input: 1->1->2->null
Output: 1->2->null

Input: 1->1->2->3->3->null
Output: 1->2->3->null
'''

class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def remove(self, head):
        if not head:
            return None

        dummy = ListNode(0)
        start = dummy

        dummy.next = head

        while head:
            if head.val != dummy.next:
                dummy = dummy.next
                dummy.next = head
            else:
                pass

            head = head.next

        dummy.next.next = None
        return start.next