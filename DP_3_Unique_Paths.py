'''
A robot is located at the top-left corner of a m x n grid.
The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom-right corner of the grid.
How many possible unique paths are there?
'''

class Solution:
    def unqiue_pathes(self, m, n):
        # 开辟一个二维动态数组
        dp = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):

            for j in range(n):

                if i == 0 or j == 0:

                    dp[i][j] = 1

                    continue

                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[i][j]

if __name__ == "__main__":
    s = Solution()
    m, n = 3, 3
    print(s.unqiue_pathes(m,n))


class Solution2:
    """
    @param m: positive integer (1 <= m <= 100)
    @param n: positive integer (1 <= n <= 100)
    @return: An integer
    """
    def uniquePaths(self, m, n):
        # write your code here
        # create 1D array
        dp = [0 for _ in range(n)]

        dp[0] = 1

        for i in range(m):
            for j in range(1, n):
                dp[j] = dp[j-1] + dp[j]

        return dp[n-1]