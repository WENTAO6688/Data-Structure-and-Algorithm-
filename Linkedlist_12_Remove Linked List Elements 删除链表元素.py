'''
Remove all elements from a linked list of integers that have value val.

Input: head = 1->2->3->3->4->5->3->null, val = 3
Output: 1->2->4->5->null

Input: head = 1->1->null, val = 1
Output: null
'''

class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param head: a ListNode
    @param val: An integer
    @return: a ListNode
    """

    def removeElements(self, head, val):
        # write your code here
        if not head:
            return head

        dummy = ListNode(0)
        tail = dummy

        while head:
            if head.val != val:
                tail.next = head
                tail = head
            head = head.next

        tail.next = None

        return dummy.next