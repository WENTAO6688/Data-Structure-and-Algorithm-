""""""
'''
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. 
A subtree of s is a tree consists of a node in s and all of this node's descendants. 
The tree s could also be considered as a subtree of itself.

Given tree s:

     3
    / \
   4   5
  / \
 1   2
 
 Given tree t:
   4 
  / \
 1   2
'''

class TreeNode(object):
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class Solution:
    def is_subtree(self, s, t):

        if not s and not t:
            return True

        if not s or not t:
            return False

        if self.is_sametree(s, t):
            return True

        return self.is_subtree(s.left, t) or self.is_subtree(s.right, t)

    def is_sametree(self, s, t):
        if not s:
            return False

        if not t:
            return True

        if s.val != t.val:
            return False

        return self.is_sametree(s.left, t.left) and self.is_sametree(s.right, t.right)

