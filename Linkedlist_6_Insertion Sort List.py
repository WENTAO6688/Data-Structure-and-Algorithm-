'''
Sort a linked list using insertion sort.

Input: 0->null
Output: 0->null

Input:  1->3->2->0->null
Output :0->1->2->3->null
'''
'''
只要当head存在时，每次都去比较后面和head的值
然后head向后移动
'''
class listNode(object):
     def __init__(self, val):
         self.val = val
         self.next = None

class Solution:
    def insertion_sort_list(self, head):
        if not head:
            return None

        tail = head
        point = listNode(0)

        while head:
            point = head
#       0 -> 1 -> 3 -> 2 -> null
            while point:
                if point.val < head.val:
                    head.val, point.val = point.val, head.val
                else:
                    point = point.next

            head = head.text

        return tail