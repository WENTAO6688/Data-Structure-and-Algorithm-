''''''
'''
Invert a binary tree.Left and right subtrees exchange.
Input: {1,3,#}
Output: {1,#,3}
Explanation:
	  1    1
	 /  =>  \
	3        3
Input: {1,2,3,#,#,4}
Output: {1,3,2,#,4}
Explanation: 
      1         1
     / \       / \
    2   3  => 3   2
       /       \
      4         4
'''
class Solution:

    def invert_binary_tree(self, root):

        if not root:
            return None

        stack = [[root]]

        while stack:

            queue = []

            nodes = stack.pop()

            for node in nodes:

                if node.left or node.right:

                    node.left, node.right = node.right, node.left

                if node.left:

                    queue.append(node.left)

                if node.right:

                    queue.append(node.right)

            if len(queue) > 0:

                stack.append(queue)
