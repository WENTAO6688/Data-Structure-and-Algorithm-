from collections import deque

class Treenode:

    def __init__(self, element):
        self.element = element
        self.left = None
        self.right = None

class Solution:
    def Level_order(self, root):
        if root is None:
            # 如果根节点不存在，则返回空列表
            return []

        # 如果存在的话，那么将存在的根节点传入一个列表中
        queue = deque([root])
        result = []
        # while循环 只要队列存在，那么我从队列中拿出最前面的元素

        while queue:
            level = []

            # 对队列中所有的元素进行判断
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.element)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        return result






