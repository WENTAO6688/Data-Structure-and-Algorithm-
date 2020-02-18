''''''
'''
Convert a binary tree to doubly linked list with in-order traversal.
      4
     / \
    2   5
   / \
  1   3
Output: 1 <->2 <->3 <->4 <->5

	    3
	   / \
	  4   1
Output:4<->3<->1

思路：
1.中序遍历将二叉树排列
2.依次去遍历有序化的二叉树元素，形成双向链表
'''
class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next, self.prev = None, None

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    def __init__(self):
        self.nums = []

    def convert_Tree_To_DLinkedList(self, root):
        if not root:
            return
        self.inorder(root)
        # we got self.nums
        return self.create_Double_linkedlist(self.nums)

    def create_Double_linkedlist(self, nums):
        if len(nums) == 0:
            return

        head = None
        prev = None

        for val in nums:
            node = ListNode(val)

            if head is None:
                head = node
            else:
                prev.next = node

            node.prev = prev
            prev = node

        return head

    def inorder(self, root):
        if not root:
            return

        self.inorder(root.left)
        self.nums.append(root.val)
        self.inorder(root.right)
