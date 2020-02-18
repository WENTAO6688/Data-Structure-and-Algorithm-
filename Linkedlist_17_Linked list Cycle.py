''''''
'''
Given a linked list, determine if it has a cycle in it.

Input: 21->10->4->5, then tail connects to node index 1 (value10).
Output: true

Input: 21->10->4->5->null
Output: false
'''
'''
思路1：快慢指针去看是否存在快慢指针相同的情况，如果有，则True
思路2：head节点是否与reverse之后的head节点相同 如果相同，则说明True
'''
class Solution1:
    def has_cycle(self, head):

        if not head or not head.next:
            return False

        slow = head
        fast = head

        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False

class Solution2:

    def has_cycle(self, head):

        if not head or not head.next:
            return False

        return head == self.reverse(head)

    def reverse(self, head):

        prev = None
        cur = head

        while cur:
            Next = cur.next
            cur.next = prev
            prev = cur
            cur = Next

        return prev
    

