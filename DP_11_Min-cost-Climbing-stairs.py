'''
在楼梯上，每一号台阶都有各自的费用，即第 i 号台阶有非负成本cost [i]（台阶从0号索引）
一旦你支付了费用，你可以爬一到两步。 你需要找到最低成本来到达最高层，你可以从索引为0的楼梯开始，也可以从索引为1的楼梯开始
'''
'''
example1:
input : cost = [10,15,20]
output: 15
example2:
input: cost = [1,100,1,1,1,100,1]
output: 6
'''

class Solution:

    def min_cost(self, cost):

        if not cost:

            return 0

        if len(cost) <= 2:

            return min(cost)

        n = len(cost)

        dp = [0 for _ in range(n)]

        dp[0], dp[1] = cost[0], cost[1]

        for i in range(2, n+1):

            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]

        return min(dp[n-2], dp[n-1])

if __name__ == " __main__":

    cost = [10, 15, 20]

    s = Solution()

    print(s.min_cost(cost))



