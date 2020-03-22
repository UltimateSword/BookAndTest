"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?



来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/unique-paths
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if n == 0:
            return 0
        dp = [[1] * n for _ in range(m)]  # m*n array
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
        return dp[m-1][n-1]


class Solution2:
    def uniquePathsWithObstacles(self, obstacleGrid: list) -> int:
        if len(obstacleGrid) == 0 or len(obstacleGrid[0]) == 0:
            return 0
        dp = [[0] * len(obstacleGrid[0])] * len(obstacleGrid)
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    if i == 0 and j == 0:
                        dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0
                    elif i == 0 and j > 0:
                        dp[i][j] = dp[i][j-1]
                    elif j == 0 and i > 0:
                        dp[i][j] = dp[i-1][j]
                    else:
                        dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]


if __name__ == '__main__':
    s = Solution()
    print(s.uniquePaths(7, 3))