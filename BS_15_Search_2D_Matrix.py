''''''
'''
Write an efficient algorithm that searches for a value in an m x n matrix.
This matrix has the following properties:
        Integers in each row are sorted from left to right.
        The first integer of each row is greater than the last integer of the previous row.

Input:  [[5]],2
Output: false
	
Input:  
[[1, 3, 5, 7],
[10, 11, 16, 20],
[23, 30, 34, 50]
],3
	
Output: true
'''

class Solution:
    def searchMatrix(self, mmatrix, target):

        if len(mmatrix) == 0 or len(mmatrix[0]) == 0:
            return False

        m, n = len(mmatrix), len(mmatrix[0])
        x, y = 0, n-1

        while x < m and y >= 0:
            goal = mmatrix[x][y]

            if goal < target:
                x += 1

            elif goal > target:
                y -= 1

            else:
                return True

        return False

if __name__ == "__main__":
    s = Solution()
    matrix = [[1,2,3],[5,6,7]]
    target = 5
    print(s.searchMatrix(matrix, target))



