'''
Given a m x n grid filled with non-negative numbers
find a path from top left to bottom right which minimizes the sum of all numbers along its path.
'''
'''
example:
[
[1,3,1],
[1,5,1],
[4,2,1]
]
output : 7
explanation: path is : 1 -> 3 -> 1 -> 1 -> 1
'''
'''
解题思路：
需要不断更新来时的路径总和
dp[i][j] 代表从(0, 0) 到点(i, j)的路径和
如果 i==0 则表示只走第一行
如果 j==0 则表示只走第一列
如果 i>0 and j>0 则表示要求得两天路径中的最小值
'''
class Solution:
    def minimum_path(self, grid):
        if len(grid) == 0 and len(grid[0]) == 0:
            return 0

        m, n = len(grid), len(grid[0])

        for i in range(m):

            for j in range(n):

                if i == 0 and j > 0:

                    grid[i][j] += grid[i][j-1]

                elif j == 0 and i > 0:
                    grid[i][j] += grid[i-1][j]

                elif i > 0 and j > 0:
                    grid[i][j] += min(grid[i][j-1], grid[i-1][j])

        return grid[m-1][n-1]

if __name__ == "__main__":
    s = Solution()
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    print(s.minimum_path(grid))