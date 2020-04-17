"""
On a N * N grid, we place some 1 * 1 * 1 cubes.

Each value v = grid[i][j] represents a tower of v cubes placed on top of grid cell (i, j).

Return the total surface area of the resulting shapes.

 

Example 1:

Input: [[2]]
Output: 10
Example 2:

Input: [[1,2],[3,4]]
Output: 34
Example 3:

Input: [[1,0],[0,2]]
Output: 16
Example 4:

Input: [[1,1,1],[1,0,1],[1,1,1]]
Output: 32
Example 5:

Input: [[2,2,2],[2,1,2],[2,2,2]]
Output: 46
 

Note:

1 <= N <= 50
0 <= grid[i][j] <= 50

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/surface-area-of-3d-shapes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def surfaceArea(self, grid: list) -> int:
        ans = 0
        for num in range(len(grid)):
            one = grid[num]
            for i in range(len(one)):
                ans += 2 + 4 * one[i] if one[i] > 0 else 0
                ans -= min(one[i], one[i+1])*2 if i != (len(one) - 1) else 0
                ans -= min(one[i], grid[num+1][i])*2 if num != (len(grid) - 1) else 0
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.surfaceArea([[1,0],[0,2]]))
