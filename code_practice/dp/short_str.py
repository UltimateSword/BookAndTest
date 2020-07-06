"""
Given a m x n grid filled with non-negative numbers,
find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.


链接：https://leetcode-cn.com/problems/minimum-path-sum

"""


class Solution:
    def minPathSum(self, grid: list) -> int:
        if not grid:
            return 0
        dp = [[0] * len(grid[0]) for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    dp[i][j] = grid[0][0]
                elif i == 0 and j > 0:
                    dp[i][j] = dp[0][j-1] + grid[0][j]
                elif i > 0 and j == 0:
                    dp[i][j] = dp[i-1][0] + grid[i][0]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[-1][-1]


if __name__ == '__main__':
    s = Solution()
    print(s.minPathSum([[1, 3, 1],
      [1, 5, 1],
      [4, 2, 1]
    ]))
