
class Treenode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    def kthsmallest(self, root, k):

        if root is None:
            return

        # 中序遍历来使其有序化
        stack, output = [], []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()
            output.append(node.val)
            node = node.right

        return output[k-1]
    

