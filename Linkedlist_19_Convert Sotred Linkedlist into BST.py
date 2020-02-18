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

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    def sortedListToBST(self, head):
        if not head:
            return None
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        return self.createBST(nums, 0, len(nums)-1)

    def createBST(self, nums, start, end):
        if not nums:
            return

        if start > end:
            return None

        if start == end:
            return TreeNode(nums[start])

        root = self.createBST(nums[(start + end) // 2])
        root.left = self.createBST(nums, start, (start + end) // 2 - 1)
        root.right = self.createBST(nums, (start + end) // 2 + 1, end)
