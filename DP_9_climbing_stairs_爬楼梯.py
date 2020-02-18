'''
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''
"""
解题思路：
初始化地面的值
在地面上的时候 down = 0
第一层台阶的时候 this = 1

第二层台阶 可以从第0层迈两步上来
可以从第1层迈一步上来

down, this = this, down + this
"""

class Solution:

    def climbing_stairs(self, n):

        if not n:

            return 0

        down, this = 0, 1

        for _ in range(n):

            down, this = this, down + this

        return this

if __name__ == "__main__":

    n = 3

    s = Solution()

    print(s.climbing_stairs(n))