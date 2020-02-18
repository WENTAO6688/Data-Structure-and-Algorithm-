''''''
'''
给定一个单链表L: L0→L1→…→Ln-1→Ln,
重新排列后为：L0→Ln→L1→Ln-1→L2→Ln-2→
必须在不改变节点值的情况下进行原地操作
'''
class ListNode(object):

    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:

    def reorder_list(self, head):
        if not head or head.next:
            return head
        mid = self.find_mid(head)
        reverse = self.reverse(mid.next)
        mid.next = None

        return self.merge(head, reverse)

    def find_mid(self, head):
        if not head or not head.next:
            return head
        slow = head
        fast = head

        while fast and fast.next and fast.next:
            slow = slow.next
            fast = fast.next
        return slow

    def reverse(self, head):
        prev = None
        cur = head

        while cur:
            Next = cur.next
            cur.next = prev
            prev = cur
            cur = Next
        return prev

    def merge(self, first, second):
        dummy = ListNode(0)
        dummy.next = first

        while first and second:
            temp_first = first.next
            temp_second = second.next

            first.next = second
            second.next = temp_first

            first = temp_first
            second = temp_second

        return dummy.next