'''
Given a string s and a dictionary of words dict,
determine if s can be broken into a space-separated sequence of one or more dictionary words.
'''
'''
Example 1:
Input: "lintcode", ["lint", "code"]
Output: true

Example 2:
Input: "a", ["a"]
Output: true
'''


class Solution:

    def wordbreak(self, string, dict):

        if not dict and not string:

            return True

        n = len(string)

        dp = [False] * (n+1)

        # initialization
        dp[0] = True

        for i in range(1, n + 1):

            for word in dict:

                if dp[i-len(word)] and string[i-len(word):i] == word:

                    dp[i] = True

        return dp[-1]