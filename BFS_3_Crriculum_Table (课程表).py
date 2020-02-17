# Description:
'''There are a total of n courses you have to take, labeled from 0 to n - 1.
Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?'''
from collections import deque
class Solution:
    def canFinish(self, numCourses, Prerequisite):
        '''
        :param numCourses: the number of courses
        :param Prerequisite:
        :return:
        '''
        # 第一步：创建每个点的入度和其邻居
        # 第二步：创建空列表存储入度为0的点
        # 第三步：对入度不为0的点， 将其的邻边减1
        Neiborhood = {x: [] for x in range(numCourses)}
        Indegree = [0 for x in range(numCourses)]
        for i, j in Prerequisite:
            Neiborhood[j].append(i)
            Indegree[i] += 1

        queue, count = deque([]), 0
        for num in range(numCourses):
            if Indegree[num] == 0:
                queue.append(num)

        while queue:
            node = queue.popleft()
            count +=1

            for number in Neiborhood[node]:
                Indegree[number] -= 1
                if Indegree[number] == 0:
                    queue.append(number)

        return numCourses == count

