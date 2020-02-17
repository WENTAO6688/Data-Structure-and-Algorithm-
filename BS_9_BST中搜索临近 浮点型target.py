# BST二叉搜索树中寻找靠近某一浮点型target的元素下标
'''
example:
root = [1,2,6,#, 7, 9,4,5]
target = 7.127842
should return  4
'''
class TreeNode:
    def __init__(self, val):

        self.val = val
        self.left, self.right = None, None

class Solution:
    def bst_search_target(self, root, target):

        upper = root
        lower = root

        while root:

            if root.val > target:
                upper = root.val
                root = root.left

            elif root.val < target:
                lower = root.val
                root = root.right

            else:
                # root.val = target
                return root.val

        if abs(upper.val - target) > abs(lower.val - target):

            return lower.val

        return upper.val


