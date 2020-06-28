"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?


链接：https://leetcode-cn.com/problems/longest-increasing-subsequence

"""


class Solution:
    def lengthOfLIS(self, nums: list) -> int:
        if not nums:
            return 0
        n = len(nums)
        dp = [(0, 0) for _ in range(n)]
        dp[0] = (nums[0], 1)
        ans = 0
        for i in range(1, n):
            one = 0
            for j in dp[:i]:
                if j[0] < nums[i]:
                    one = max(one, j[1])
            dp[i] = (nums[i], one+1)
            ans = max(ans, one+1)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLIS([10,9,2,5,3,4]))
    print(s.lengthOfLIS([10,9,2,5,3,7,101,18]))
    print(s.lengthOfLIS([1,3,6,7,9,4,10,5,6]))