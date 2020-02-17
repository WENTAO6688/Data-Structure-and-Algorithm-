class TreeNode:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

class Solution:
    def Serialize(self, root):
        if not root:
            return {}

        queue = [root]
        index = 0

        while index < len(queue):
            if queue[index] is not None:
                queue.append(queue[index].left)
                queue.append(queue[index].right)
            index += 1

        while queue[-1] is None:
            queue.pop()

        return '{%s}' % ','.join([str(node.val)] if node is not None else '#'
                                 for node in queue)

    def deserialize(self, data):
        data = data.strip('\n')

        if data == '{}':
            return None

        values = data[1:-1].split(',')
        root = TreeNode(int[values[0]])
        queue = [root]
        is_left = True
        index = 0

        for val in values[1:]:
            if val is not '#':
                node = TreeNode(int(val))
                if is_left:
                    queue[index].left = node
                else:
                    queue[index].right = node

            if not is_left:
                index += 1

            is_left = not is_left

        return root




