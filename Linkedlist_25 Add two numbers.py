'''
You have two numbers represented by a linked list, where each node contains a single digit. The digits are stored in reverse order,
such that the 1's digit is at the head of the list. Write a function that adds the two numbers and returns the sum as a linked list.

Input: 7->1->6->null, 5->9->2->null
Output: 2->1->9->null
Explanation: 617 + 295 = 912, 912 to list:  2->1->9->null

Input:  3->1->5->null, 5->9->2->null
Output: 8->0->8->null
Explanation: 513 + 295 = 808, 808 to list: 8->0->8->null
'''

class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def add_numbers(self, l1, l2):
        """
        :param l1: ListNode
        :param l2: ListNode
        :return: List
        """
        dummy = ListNode(None)
        tail = dummy
        carry = 0

        while l1 or l2 or carry:
            num = 0
            if l1:
                num += l1.val
                l1 = l1.next

            if l2:
                num += l2.val
                l2 = l2.next

            num += carry

            digit, carry = num % 10, num // 10

            node = ListNode(digit)

            tail.next, tail = node, node

        return dummy.next


