'''
'A' -> 1
'B' -> 2
'Z' -> 26

Input: "12"
Output: 2
Explanation: It could be decoded as AB (1 2) or L (12).

Input: "10"
Output: 1
'''
class Solution:
    def decode_ways(self, s):
        # edge case
        if s == '' or len(s) == 0 or s[0] == '0':
            return 0
        # Initialize a Array
        dp = [1, 1]

        for i in range(2, len(s) + 1):
            if 10 <= int(s[i-2: i]) <= 26 and int(s[i-1]) != 0:
                dp.append(dp[i-1] + dp[i-2])

            elif int(s[i-2:i]) == 10 or int(s[i-2:i]) == 20:
                dp.append(dp[i-2])

            elif s[i-1] != '0':
                dp.append(dp[i-1])

            else:
                return 0

        return dp[len(s)]

if __name__ == "__main__":
    s = '1234'
    a = Solution()
    print(a.decode_ways(s))
