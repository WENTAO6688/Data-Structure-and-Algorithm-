"""
return the length of longest continuous increasing sub-sequence.
the longest continuous increasing sub-sequence could be valid no matter from left to right or from right to left.
"""
"""
for example:
[1,2,3,4,1]
output: 4

[5,4,2,1,5]
output: 4
"""

"""
遍历所有的值
如果后一个的值大于前一个的值，那么递增情况下的变量 increase = increase + 1
如果后一个的值小于前一个的值，那么递减情况下的变量 decrease = decrease + 1
如果前后的值相等，那么 decrease = increase = 1
"""

def the_longest_continuous_increasing_sussequence(A):
    if not A:
        return None
    # initialization
    increase, decrease, longest = 1, 1, 1

    for i in range(len(A)):
        if A[i] > A[i-1]:
            increase += 1
            decrease = 1

        elif A[i] < A[i-1]:
            decrease += 1
            increase = 1

        else:
            # A[i] == A[i-1]
            decrease = 1
            increase = 1

        longest = max(longest, max(increase, decrease))

    return longest

A = [1,2,3,4,5,6,1,2,3,7]

a = the_longest_continuous_increasing_sussequence(A)

print(a)




