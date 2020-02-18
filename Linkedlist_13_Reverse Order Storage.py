'''
Give a linked list, and store the values of linked list in reverse order into an array.

Input: 1 -> 2 -> 3 -> null
Output: [3,2,1]

Input: 4 -> 2 -> 1 -> null
Output: [1,2,4]
'''
class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def reverse_order_storage(self, head):

        list = []

        while head:
            list.insert(0, head.val)
            head = head.next

        return list
