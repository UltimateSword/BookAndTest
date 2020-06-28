"""
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"


链接：https://leetcode-cn.com/problems/longest-valid-parentheses

"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        dp = [0] * len(s)
        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i-1] == '(':
                    dp[i] = dp[i-2] + 2 if i > 2 else 2
                elif i - dp[i-1] - 1 >= 0 and s[i - dp[i-1] - 1] == '(':
                    if i - dp[i-1] -2 > 0:
                        dp[i] = dp[i-1] + 2 + dp[i - dp[i-1] -2]
                    else:
                        dp[i] = dp[i-1] + 2
        return max(dp)


if __name__ == '__main__':
    s = Solution()
    print(s.longestValidParentheses("(()))())("))