"""
Given an array of integers A, a move consists of choosing any A[i], and incrementing it by 1.

Return the least number of moves to make every value in A unique.

 

Example 1:

Input: [1,2,2]
Output: 1
Explanation:  After 1 move, the array could be [1, 2, 3].
Example 2:

Input: [3,2,1,2,1,7]
Output: 6
Explanation:  After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
It can be shown with 5 or less moves that it is impossible for the array to have all unique values.
 

Note:

0 <= A.length <= 40000
0 <= A[i] < 40000


链接：https://leetcode-cn.com/problems/minimum-increment-to-make-array-unique

"""


class Solution:
    def minIncrementForUnique(self, A: list) -> int:
        count = [0] * len(A) * 2
        for i in A:
            count[i] += 1
        ans = token = 0
        for i in range(len(count)):
            if count[i] >= 2:
                token += count[i] - 1  # 要向后寻找多少个数
                ans -= i * (count[i] - 1)
            elif token > 0 and count[i] == 0:  # 跳过已经被占据的数
                ans += i
                token -= 1  # 找到了一个
        return ans

    def main(self, A):
        A.sort()
        n = len(A)
        dp = [0 for _ in range(n)]
        for i in range(1, n):
            check = set(A[:i])
            dp[i] = dp[i - 1]
            while A[i] in check:
                A[i] += 1
                dp[i] += 1
        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    print(s.minIncrementForUnique([3,2,1,2,1,7]))
