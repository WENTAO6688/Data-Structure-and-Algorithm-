class Solution:

    def can_finish(self, numbers, prerequisite):
        # 创建字典来储存所有课程本身及其邻边
        neighbors = {x : [] for x in range(numbers)}
        indegree = [0 for x in range(numbers)]

        # 将所有课程的入度加到字典当中
        for i, j in prerequisite:
            neighbors[j].append(i)
            indegree[i] += 1

        # 建立queue 列表用于储存课程
        # 建立count来表示当前课程数目
        queue, count = [], 0

        # 将入度为0的课程加入到queue当中，因为它们可以直接学，没有前提条件
        for num in numbers:
            if indegree[num] == 0:
                queue.append(num)

        # 只要队列中存在元素 我们就弹出来
        while queue:
            node = queue.pop()
            # 并且课程数量加 1
            count += 1

            for neighbor in neighbors[node]:
                # 对当前课程的后续课程进行入度减1
                indegree[neighbor] -= 1
                # 如果结果刚好等于0，那么我们将等于0的课程加入到queue中
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # 循环结束后，判断当前课程的数量是否等于传入课程的数量
        return count == numbers

