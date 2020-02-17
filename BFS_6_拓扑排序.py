class Solution:

    def topological_sort(self, graph):

        # 求得所有节点的入度
        node_to_degree = self.get_indegree(graph)
        # 寻找节点为0的节点
        order = []
        start_node = [n for n in graph if node_to_degree[n] == 0]
        queue = start_node
        order.append(start_node)

        while queue:
            node = queue.pop(0)
            for neighbor in node.neighbors:
                node_to_degree[neighbor] -= 1
                if node_to_degree[neighbor] == 0:
                    order.append(neighbor)

        return order

    def get_indegree(self, graph):
        # 先求得所有节点的入度
        node_to_degree = {x:0 for x in graph}

        # 对于图中的所有节点的邻边 入度加1
        for node in graph:
            for neighbor in node.neighbors:
                node_to_degree[neighbor] += 1

        return node_to_degree
