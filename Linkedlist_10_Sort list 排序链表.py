'''
Sort a linked list in O(n log n) time using constant space complexity.

Input:  1->3->2->null
Output:  1->2->3->null

Input: 1->7->2->6->null
Output: 1->2->6->7->null

Challenge
Solve it by merge sort & quick sort separately.
'''
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def sort_list(self, head):
        if not head or not head.next:
            return head
        dummy_l = ListNode(-1)
        dummy_r = ListNode(-1)
        dummy_m = ListNode(-1)

        tail_l = dummy_l
        tail_r = dummy_r
        tail_m = dummy_m

        mid_node = self.find_mid_node(head)

        while head is not None:
            if head.val < mid_node.val:
                tail_l.next = head
                tail_l = head

            elif head.val > mid_node.val:
                tail_r.next = head
                tail_r = head

            else:
                tail_m.next = head
                tail_m = head

            head = head.next

        tail_l.next = None
        tail_r.next = None
        tail_m.next = None

        left = self.sort_list(dummy_l.next)
        right = self.sort_list(dummy_r.next)
        return self.connect(left, dummy_m.next, right)

    def find_mid_node(self, node):
        if not node:
            return node
        slow = node
        fast = node
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        mid_node = slow
        return mid_node

    def connect(self, left, mid, right):
        dummy = ListNode(0)
        cur = dummy
        cur.next = left
        while cur.next is not None:
            cur = cur.next
        cur.next = mid
        while cur.next is not None:
            cur = cur.next
        cur.next = right

        return dummy.next