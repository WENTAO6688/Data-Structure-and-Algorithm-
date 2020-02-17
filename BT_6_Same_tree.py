''''''
'''
Check if two binary trees are identical.
Identical means the two binary trees have the same structure and every identical position has the same value.
'''
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    def same_tree(self, a, b):
        if a is None and b is None:
            return True

        if a is None or b is None:
            return False

        if a.val != b.val:
            return False

        return self.same_tree(a.left, b.left) and self.same_tree(a.right, b.right)
