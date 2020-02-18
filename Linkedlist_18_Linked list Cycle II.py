class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def has_cycle(self, head):

        if not head or head.next:
            return None

        slow = head
        fast = head
        while fast and fast.head:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break

        if slow == fast:
            slow = head

            while slow != head:
                slow = slow.head
                fast = fast.head

            return slow.val

        return None