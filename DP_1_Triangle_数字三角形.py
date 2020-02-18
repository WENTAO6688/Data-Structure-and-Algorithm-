'''输入下列数字三角形：
[
[2],
[3,4],
[6,5,7],
[4,1,8,3]
]
输出： 11
解释： 从顶到底部的最小路径和为11 ( 2 + 3 + 5 + 1 = 11)。
'''
'''
第一种方法： 遍历所有的点，与初始化的最大值去打擂台 
每次记录路径最小值
把路径最小值加上点本身
'''
import sys

class Solution:
    def minimumTotal(self, triangle):
        self.minimum = sys.maxsize
        self.travesal(triangle, 0, 0, 0)
        return self.minimum

    def travesal(self, triangle, x, y, path_sum):
        if x == len(triangle):
            self.minimum = min(path_sum, self.minimum)
            return

        self.travesal(triangle, x+1, y, path_sum + triangle[x][y])
        # (1,0),(2,0),(3,0)
        self.travesal(triangle, x+1, y+1, path_sum + triangle[x][y])
        # (1,1),(2,2),(3,3)
'''
第二种方法：
记忆化搜索加分治法
创建一个memo 来记录先前访问过的点
'''

class Solution2:
    def minimumtotal(self, triangle):

        return self.divide_conquer(triangle, 0, 0, {})

    def divide_conquer(self, triangle, x, y, memo):

        if x == len(triangle):
            return 0

        if (x, y) in memo:
            return memo[(x, y)]

        left = self.divide_conquer(triangle, x+1, y, memo)
        right = self.divide_conquer(triangle, x+1, y+1, memo)

        memo[(x, y )] = min(left, right) + triangle[x][y]
        return memo[(x,y)]