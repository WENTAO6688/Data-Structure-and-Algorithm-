''''''
'''
Implement an algorithm to delete a node in the middle of a singly linked list, given only access to that node.
'''
'''
题目没有给头节点
需要先把node后面的值赋给node，然后删掉node后面的那个
'''
class Solution:
    def delete_node(self, node):
        if not node or not node.next:
            node = None
            return

        node.val = node.next.val
        node.next = node.next.next