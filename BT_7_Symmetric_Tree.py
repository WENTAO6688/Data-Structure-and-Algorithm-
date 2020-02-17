''''''
'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

Input: {1,2,2,3,4,4,3}     Output: true
Explanation:
    1
   / \
  2   2
 / \ / \
3  4 4  3
This binary tree {1,2,2,3,4,4,3} is symmetric

Input: {1,2,2,#,3,#,3}     Output: false
Explanation:
    1
   / \
  2   2
   \   \
   3    3
This is not a symmetric tree'''

class Solution:
    def is_symmeric(self, root):
        if not root:
            return True
        s = []
        s.append(root.left)
        s.append(root.right)

        while s:
            r_node = s.pop()
            l_node = s.pop()
            if r_node is None and l_node is None:
                pass

            if r_node is None or l_node is None:
                return False

            if r_node.val != l_node.val:
                return False

            s.append(r_node.right)
            s.append(l_node.left)

            s.append(r_node.left)
            s.append(l_node.right)

        return True