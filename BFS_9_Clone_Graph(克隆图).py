from collections import deque

class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    def clone_graph(self, node):
        root = node

        if node is None:
            return None
        # 将nodes求出
        nodes = self.get_node(node)
        # 创立一个字典
        mapping = {}
        # 将nodes本身和其对应的边匹配起来
        for node in nodes:
            mapping[node] = UndirectedGraphNode(node.label)
            # 复制一个新的图
        for node in nodes:
            new_node = mapping[node]
            for neighbor in node.neighbors:
                new_neighbor = mapping[neighbor]
                new_node.neighbors.append(new_neighbor)

        return mapping[root]

# 先求出克隆图的所有节点
    def get_node(self, node):
        # 建立一个队列和一个结果
        queue = deque([node])
        result = set([node])

        while queue:
            node = queue.popleft()
            for neighbor in node.neighbors:
                if neighbor not in result:
                    result.add(neighbor)
                    queue.append(neighbor)
        return result








