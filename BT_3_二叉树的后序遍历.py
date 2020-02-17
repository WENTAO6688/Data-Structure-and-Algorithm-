
class Treenode:

    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:

    def postorder_traversal(self, root):
        if root is None:

            return []

        result, stack1, stack2 = [], [root], []

        while stack1:

            node = stack1.pop()

            stack2.append(node.val)

            if node.left:

                stack1.append(node.left)

            if node.right:

                stack1.append(node.right)

        while stack2:

            result.append(stack2.pop())

        return result