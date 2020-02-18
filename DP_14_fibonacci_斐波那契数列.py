'''
'''
'''
Find the Nth number in Fibonacci sequence.A Fibonacci sequence is defined as follow:

The first two numbers are 0 and 1. The ith number is the sum of i-1 th number and i-2 th number.

0, 1, 1, 2, 3, 5, 8, 13, 21, 34...

Input: 1 Output: 0
return the first number in Fibonacci sequence.

Input: 2 Output: 1
return the second number in Fibonacci sequence.
'''

def fibonacci(n):

    if n == 0:
        return 0

    if n == 1:
        return 1

    dp = [0 for i in range(n+1)]
    # init
    dp[0], dp[1] = 0, 1

    for j in range(2, n):

        dp[j] = dp[j-2] + dp[j-1]

    return dp[n-1]

a = fibonacci(4)
print(a)
