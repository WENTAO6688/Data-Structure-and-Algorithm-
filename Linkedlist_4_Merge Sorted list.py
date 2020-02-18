'''
Merge two sorted (ascending) linked lists and return it as a new sorted list.
The new sorted list should be made by splicing together the nodes of the two lists and sorted in ascending order.
'''
'''
Input: list1 = null, list2 = 0->3->3->null
Output: 0->3->3->null

Input:  list1 =  1->3->8->11->15->null, list2 = 2->null
Output: 1->2->3->8->11->15->null
'''

"""
思路： 两个链表的node相比较 小的Node先放进去
"""

class listNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def merge_list(self, l1, l2):

        dummy = listNode(0)
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                dummy.next = l1
                l1 = l1.next

            else:
                dummy.next = l2
                l2 = l2.next

            dummy = dummy.next

        if l1:
            dummy.next= l1
        if l2:
            dummy.next = l2

        return tail.next