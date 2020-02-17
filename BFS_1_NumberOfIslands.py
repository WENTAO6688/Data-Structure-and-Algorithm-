# Given a 2D boolean Array. In this Array, 0 represents the sea and 1 represents the island.
# If two "1" are adjacent, including below/above/left/right, we will regard these "1" as the same island.
# for example:
# [[ 0, 1, 1, 0, 0 ],
#  [ 0, 1, 0, 0, 0 ],
#  [ 0, 0, 1, 1, 0 ],
#  [ 0, 0, 1, 0, 0 ],
#  [ 1, 0, 0, 0, 0 ]]
# the number of islands has to be 3
# define this 2D array as grid(网格)

# grid代表网格的意思，因为需要遍历网格中的每个点，注意此处题目是输入2D Bool的形式
# x, y 代表具体坐标的数值，例如0，1 和 1，0
# visited 代表的是已经访问过的点
from collections import deque

class Solution:

    def NumIslands(self, grid):
        Island = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] and (i, j) not in visited:
                    self.BFS(grid, i, j, visited)
                    Island += 1
        return Island

    def BFS(self, grid, x, y, visited):
        # 广度优先遍历要使用queue去做
        # queue 的特点是先进先出，我们将一个点加到队列中，对其周围的四个点依次进行访问
        queue = deque[(x, y)]
        visited.add((x, y))
        while queue:
            x, y = queue.popleft()
            for delta_x, delta_y in [(1, 0),(-1, 0),(0, 1),(0, -1)]:
                next_x = delta_x + x
                next_y = delta_y + y
                if not self.IsValid(grid, next_x, next_y, visited):
                    continue
                queue.append((next_x, next_y))
                visited.add((next_x, next_y))

    def IsValid(self, grid, x, y, visited):
        m, n = len(grid), len(grid[0])
        # 要确保不越界 并且点有效
        return  0 <= x < m and 0 <= y < n and grid[x][y] and (x, y) not in visited