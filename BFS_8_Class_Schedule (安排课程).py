class Solution:

    def findOrder(self, numCourses, prerequisites):
        edges = {x: [] for x in range(numCourses)}
        Indegree = [0 for x in range(numCourses)]

        for i,j in prerequisites:
            edges[j].append(i)
            Indegree[i] += 1

        order = []
        queue = []

        for num in range(numCourses):
            if Indegree[num] == 0:
                queue.append(num)

        while queue:
            node = queue.pop(0)
            order.append(node)

        for next_class in edges[node]:
            Indegree[next_class] -= 1
            if Indegree[next_class] == 0:
                queue.append(next_class)

        if len(order) == numCourses:
            return order
        else:
            return []


