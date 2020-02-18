'''
There is a fence with n posts, each post can be painted with one of the k colors.
You have to paint all the posts such that no more than two adjacent fence posts have the same color.
Return the total number of ways you can paint the fence.
(n and k are non-negative integers).
'''
'''
Input: n=3, k=2  
Output: 6
          post 1,   post 2,   post 3
    way1    0         0         1 
    way2    0         1         0
    way3    0         1         1
    way4    1         0         0
    way5    1         0         1
    way6    1         1         0

Input: n=2, k=2  
Output: 4
           post 1,  post 2
    way1     0        0       
    way2     0        1            
    way3     1        0          
    way4     1        1
'''
'''
dp[i] == (k-1) * (dp[i-2] + dp[i-1])  
滚动数组 O(N)
'''
class Solution:

    def painting_fence(self, n, k):

        if k == 1 and n >= 3: return 0
        if n == 0: return 0
        if n == 1: return k
        if n == 2: return k*k

        low, high = k, k*k

        for i in range(n-2):
            low, high = high, (k-1)*low + (k-1)*high

        return high

if __name__ == "__main__":
    s = Solution()
    n, k = 3, 3
    print(s.painting_fence(n, k))
