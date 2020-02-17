'''
Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.
'''

class Treenode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    def BST(self, root, target, k):
        if root is None:
            return []

        # 中序遍历
        node = root
        stack, inorder_result = [], []
        while stack or node:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()

            if len(inorder_result) >= k:
                if abs(node.val - target) > abs(inorder_result[-k] - target):
                    break
            inorder_result.append(node.val)
            node = node.right

        return inorder_result[-k:]

