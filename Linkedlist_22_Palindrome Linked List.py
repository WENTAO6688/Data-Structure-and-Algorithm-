''''''
'''
Implement a function to check if a linked list is a palindrome.

Input: 1->2->1
output: true
Input: 2->2->1
output: false
'''
'''
思路：可以找到中间节点，然后reverse后半部分
然后将两部分  从头节点开始去依次比较，如果全都相同，那就说明是回文链表 
'''
class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def isPalindrome(self, head):
        if not head or not head.next:
            return True

        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow
        second_part_head = mid.next

        second_part = self.reverse(second_part_head)

        return self.is_Palindrome(head, second_part_head)

    def reverse(self, head):
        prev = None
        cur = head

        while cur:
            Next = cur.next
            cur.next = prev
            prev = cur
            cur = Next

        return prev

    def is_Palindrome(self, first, second):

        while first and second:
            if first.val != second.val:
                return False
            else:
                first = first.next
                second = second.next

        return True

