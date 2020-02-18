'''
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
You should preserve the original relative order of the nodes in each of the two partitions.
'''
'''
Input:  list = 1->4->3->2->5->2->null, x = 3
Output: 1->2->2->4->3->5->null	
Explanation:  keep the original relative order of the nodes in each of the two partitions.
'''

'''
left:     -> 1 -> 2 -> 2
     left           left_dummy
    
right:    -> 4 -> 3 -> 5
      right          right_dummy
'''
class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def partition(self, head, x):
        if not head:
            return

        left_dummy = ListNode(0)
        right_dummy = ListNode(0)
        left = left_dummy
        right = right_dummy
        while head:
            if head.val < x:
                left_dummy.next = head
                left_dummy = left_dummy.next
            else:
                right_dummy.next = head
                right_dummy = right_dummy.next
            head = head.next

        right_dummy.next = None
        left_dummy.next = right.next

        return left.next