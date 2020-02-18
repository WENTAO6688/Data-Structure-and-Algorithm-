'''
Given a string s, find the longest palindromic subsequences length in s.
You may assume that the maximum length of s is 1000.
'''
class Solution:

    def subsequences(self, string):

        n = len(string)
        dp = [[0 for i in range(n)] for j in range(n)]

        for i in range(n):
            dp[i][i-1] = 0
            dp[i][i] = 1

        for length_i_to_j in range(2, n+1):
            for i in range(n - length_i_to_j + 1):
                j = i + length_i_to_j -1

            if string[i] == string[j] and length_i_to_j == 2:
                dp[i][j] = 2

            elif string[i] == string[j]:
                dp[i][j] = 2 + dp[i+1][j-1]

            else:
                dp[i][j] = max(dp[i][j-1],dp[i+1][j])

        return dp[0][n-1]

if __name__ == "__main__":
    s = Solution()
    string = 'abbac'
    print(s.subsequences(string))
