''''''
'''
Find the maximum node in a binary tree, return the node.
Input: {1,-5,3,1,2,-4,-5}
Output: 3

The tree look like this:
     1
   /   \
 -5     3
 / \   /  \
1   2 -4  -5
'''

class Solution:
    def maxNode(self, root):
        if not root:
            return None

        left = self.maxNode(root.left)
        right = self.maxNode(root.right)
        return self.max(root, self.max(left, right))

    def max(self, a, b):
        if not a:
            return b
        if not b:
            return a
        if a.val > b.val:
            return a
        return b

