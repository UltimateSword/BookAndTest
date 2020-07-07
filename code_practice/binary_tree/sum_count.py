# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        ans = False

        def recall(now, lft, rgt):
            nonlocal ans
            if lft is None and rgt is None:
                if now == sum:
                    ans = True
                return

            if lft:
                recall(now+lft.val, lft.left, lft.right)
            if rgt:
                recall(now+rgt.val, rgt.left, rgt.right)

        if root:
            recall(root.val, root.left, root.right)
        return ans