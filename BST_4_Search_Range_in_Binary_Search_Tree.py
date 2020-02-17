'''
Given a binary search tree and a range [k1, k2], return node values within a given range in ascending order.
'''
'''
Input：{20,8,22,4,12},10,22
Output：[12,20,22]
Explanation：
        20
       /  \
      8   22
     / \
    4   12
it will be serialized {20,8,22,4,12}
[12,20,22] between 10 and 22
'''
# 思路1：因为是二叉搜索树，中序遍历后使其成为有序数组，然后去判断
# 思路2：DFS递归
'''
递归的出口是，如果当前节点不存在，那么停止
1. 如果根节点的值 < k1, 那么可以肯定左子树的值不在可求范围内。if root.val < k1: 去看右子树
2. 如果根节点的值在[k1, k2]范围内，那么将其加入到结果当中
3. 如果根节点的值 > k2, 那么可以肯定右子树的值不在可求范围内。if root.val > k2：去看左子树
'''
class Solution:
    def search_range(self, root, k1, k2):
        if not root:
            return
        result = []
        self.dfs(root, k1, k2, result)
        return result

    def dfs(self, root, k1, k2, result):
        if not root:
            return
        if root.val < k1:
            self.dfs(root.right, k1, k2, result)
        if root.val >= k1 and root.val <= k2:
            result.append(root.val)
        if root.val > k2:
            self.dfs(root.left, k1, k2, result)