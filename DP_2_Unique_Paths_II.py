class Solution:

    def unique_pathII(self, obstacle):

        if not obstacle or len(obstacle) == 0 or not obstacle[0] or len(obstacle) == 0:
            return None

        m, n = len(obstacle), len(obstacle[0])

        dp = [[0 for _ in range(m)] for _ in range(n)]

        for i in range(m):

            for j in range(n):

                if obstacle[i][j] > 0:
                    dp[i][j] = 0
                    continue

                if i == 0 and j == 0:
                    dp[i][j] = 1

                elif i == 0:
                    dp[i][j] = dp[i][j-1]

                elif j == 0:
                    dp[i][j] = dp[i-1][j]

                else:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j]

        return dp[m-1][n-1]





