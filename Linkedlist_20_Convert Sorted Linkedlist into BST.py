''''''
'''
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
Input: array = 1->2->3    Output:
                                             2
                                           /   \
                                          1     3
Input: 2->3->6->7         Output:
                                            3
                                           / \
                                          2   6
                                                \
                                                  7
'''
class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class Treenode(object):
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    def sorted_list_into_BST(self, head):
        if not head:
            return

        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow
        mid.next = None
        root = Treenode(slow.val)

        root.left = self.sorted_list_into_BST(head)
        root.right = self.sorted_list_into_BST(mid.next)

        return root
