"""
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \
      4   5
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/diameter-of-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

实际上这利用了 max 的性质，
max 是一种在线算法。
简单来说，在线算法就是在计算的时候，所有的输入数据以“流”的形式一个个进来，
算法每次只处理一条数据，不需要保存全部的数据。
"""


class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        self.ans = 1

        def dp(node):
            if not node:
                return 0
            L = dp(node.left)
            R = dp(node.right)
            self.ans = max(self.ans, L+R+1)
            return max(L+R) + 1  # 返回最大深度
        dp(root)
        return self.ans - 1

    def diameterOfBinaryTree_quick(self, root) -> int:
        self.ans = 1

        def dp(node):
            if not node:
                return 0
            L = dp(node.left)
            R = dp(node.right)
            self.ans = max(self.ans, L + R + 1)
            return max(L + R) + 1  # 返回最大深度

        dp(root)
        return self.ans - 1