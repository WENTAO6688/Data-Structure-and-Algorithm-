class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    def __init__(self, root):
        # 定义根结点前的假节点
        dummy  =TreeNode(0)
        dummy.right = root
        self.stack = [dummy]
        self.next()


    def hasnext(self):
        return bool(self.stack)

    def next(self):
        # 因为要求下一个的最小值
        # 所以要先添加右边的 后添加左边的
        node = self.stack.pop()
        node_next = node
        if node.right:
            node = node.right

            while node:
                self.stack.append(node)
                node = node.left
        return node_next