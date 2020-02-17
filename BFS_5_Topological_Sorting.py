"""
Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""

class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        # write your code here
        node_to_degree = self.get_degree(graph)

        # 创建一个order列表来存储即将进入的节点
        order = []

        # 寻找入度为0的节点
        start_nodes = [n for n in graph if node_to_degree[n] == 0]
        queue = start_nodes

        # 更简洁的写法来指明，入度为0的节点，也就是图开始的节点
        # queue = [n for n in graph if node_to_degree[n] == 0]
        
        while queue:
            node = queue.pop[0]
            order.append(node)

            for neighbors in node.neighbors:
                node_to_degree[neighbors] -=1
                if node_to_degree[neighbors] == 0:
                    order.append(neighbors)
        return order


    def get_degree(self, graph):

        node_to_degree = {x:0 for x in graph}

        for node in graph:
            for neighbors in node.neighbors:
                node_to_degree[neighbors] += 1
        return node_to_degree

