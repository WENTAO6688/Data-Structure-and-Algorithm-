class Solution:

    def myPow(self, x, n):
        # 判断指数为负数的情况
        if n <0:
            x = 1/x
            n = -n

        ans = 1
        tmp = x

        while n != 0:
            # 如果指数是奇数
            if n % 2 == 1:
                ans *= tmp
            # 是偶数幂
            tmp *= tmp
            n //= 2
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.myPow(2,3))