'''
'''
'''
There is a stone game.At the beginning of the game the player picks n piles of stones in a line.
The goal is to merge the stones in one pile observing the following rules:

1. At each step of the game, the player can merge two adjacent piles to a new pile.
2. The score is the number of stones in the new pile.
You are to determine the minimum of the total score.
'''
"""
方法一：记忆化搜索最小值，时间复杂度 O(n^3)
"""
import sys

def Stone_Game(A):
    return helper(A, 0, len(A)-1, {})

def helper(A, start, end, memo):
    # 递归出口
    if (start, end) in memo:
        return memo[(start, end)]

    if start >= end:
        return 0

    minimum = sys.maxsize
    cost = sum(A[start: end+1])

    for mid in range(start, end):
        left = helper(A, start, mid, memo)
        right = helper(A, mid+1, end, memo)
        minimum = min(minimum, left + right + cost)

    memo[(start, end)] = minimum
    return minimum
