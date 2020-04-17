"""
Given two binary trees, write a function to check if they are the same or not.
给两个二叉树,吮吸Ian一个函数可以判断是否他们相同.
Two binary trees are considered the same if they are structurally identical and the nodes have the same value.
二叉树结构和节点 相同被认为是相同的二叉树
Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false
Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/same-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        ans = []

        def walk(node, node1):
            if not node:
                return node1 is None
            if not node1:
                return node is None
            if node.val != node1.val:
                return
            ans.append(node.val)
            walk(node.left, node1.left)
            walk(node.right, node.right)

        stack = []
        node1 = p
        node2 = q
        while stack and node1:
            while node1:
                stack.append(node1)
                node2 = node2.left
                node1 = node1.left
            one = stack.pop()



