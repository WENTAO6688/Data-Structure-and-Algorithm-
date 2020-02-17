''''''
'''
Given a sorted (increasing order) array, Convert it to create a binary search tree with minimal height.
Input: [1,2,3,4,5,6,7]
Output:  {4,2,6,1,3,5,7}
Explanation:
A binary search tree with minimal height.

         4
       /   \
      2     6
     / \    / \
    1   3  5   7
思路：
1 每次找出列表的中间节点 然后分别去递归左右子树
'''
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
        
class Solution:
    def sorted_array_to_BST(self, A):
        return self.convert(A)

    def convert(self, A):
        if not A:
            return None

        mid = (len(A) - 1) // 2
        root = TreeNode(A[mid])
        root.left = self.convert(A[:mid])
        root.right = self.convert(A[mid+1:])
        return root
