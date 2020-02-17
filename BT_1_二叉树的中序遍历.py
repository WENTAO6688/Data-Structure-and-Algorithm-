# 二叉树的中序遍历

class Treenode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

# 非递归版本
class Solution:
    def inorder_traversal(self, root):
        if root is None:
            return []

        output, stack= [],[]
        node = root

        while stack or node:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()
            output.append(node.val)
            node = node.right

        return output

# 递归版本
class Solution2:
    def inorder(self, node):
        self.stack = []
        self.inorder_travesal(node)
        return self.stack

    def inorder_travesal(self, node):
        if node is None:
            return []
        self.inorder_travesal(node.left)
        self.stack.append(node.val)
        self.inorder_travesal(node.right)






