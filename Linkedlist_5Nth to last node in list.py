'''
Find the nth to last element of a singly linked list.
The minimum number of nodes in list is n.

Input: list = 3->2->1->5->null, n = 2
Output: 1

Input: list  = 1->2->3->null, n = 3
Output: 1
'''

'''
快慢指针
先让head走n个，然后head和slow一起走
当head为None的时候，slow那个就是要return的值
time complexity: O(n)
space complexity: O(1)
'''
class Solution:
    def the_last_Nth_node(self, head, n):
        if not head:
            return

        slow = head

        for i in range(n):
            head = head.next

        while head:
            head = head.next
            slow = slow.next

        return slow