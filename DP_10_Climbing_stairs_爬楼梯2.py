'''
A child is running up a staircase with n steps, and can hop either 1 step, 2 steps, or 3 steps at a time.
Implement a method to count how many possible ways the child can run up the stairs.
一个小孩爬一个 n 层台阶的楼梯。他可以每次跳 1 步， 2 步 或者 3 步。实现一个方法来统计总共有多少种不同的方式爬到最顶层的台阶。
'''

class Solution:

    def climbingstairs2(self, n):

        if n <= 1:

            return 1

        if n == 2:

            return 2

        a,b,c = 1,1,2

        for i in range(3, n+1):

            a,b,c = b,c,a+b+c

        return c

if __name__ == "__main__":

    s = Solution()

    print(s.climbingstairs2(5))

