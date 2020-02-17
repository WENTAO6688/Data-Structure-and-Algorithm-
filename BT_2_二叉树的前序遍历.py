class Treenode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

# 递归版本
class Solution1:
    def preorder_traversal(self, root):
        # 创建一个stack
        self.stack = []
        # 遍历根结点
        self.traversal(root)
        return self.stack

    def traversal(self, root):
        if root is None:
            return

        self.stack.append(root.val)
        self.traversal(root.left)
        self.traversal(root.right)

# 非递归版本
class Solution2:

    def preorder(self, root):
        if root is None:
            return

        result, stack =[], [root]

        while stack:

            node = stack.pop()
            result.append(node.val)

            if node.right:
                stack.append(node.right)

            if node.left:
                stack.append(node.left)

            return result