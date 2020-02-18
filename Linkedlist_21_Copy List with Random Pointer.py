''''''
'''
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.
Return a deep copy of the list.'''

"""
思路：
1. 建立一个哈希表 去映射每个节点 —> label
2. for循环哈希表中的key，如果key的next 存在 映射进去， 同理random

"""
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    def deepcopy(self, head):
        if not head:
            return None

        hash_map = {}
        cur = head
        while cur:
            hash_map[cur] = RandomListNode(head.label)
            cur = cur.next

        for nodes in hash_map:
            if nodes.next:
                hash_map[nodes].next = hash_map[nodes.next]
            if nodes.random:
                hash_map[nodes].random  = hash_map[nodes.random]

        return hash_map[head]
