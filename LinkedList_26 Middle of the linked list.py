'''
Given a non-empty, singly linked list with head node head, return a middle node of linked list.
If there are two middle nodes, return the second middle node.
'''
'''
Input: 1->2->3->4->5->null
Output: 3->4->5->null

Input: 1->2->3->4->5->6->null
Output: 4->5->6->null
'''
"""
快慢指针
"""
class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def get_middle(self, head):

        if not head or not head.next:
            return head

        slow = head
        fast = head.next

        while head.next is not None and head.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow.next
