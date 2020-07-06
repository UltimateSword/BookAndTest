"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).


链接：https://leetcode-cn.com/problems/decode-ways

"""


class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * len(s)
        if s[0] == '0':
            return 0
        if len(s) == 1:
            return 1
        dp[0] = 1
        if s[1] == '0' and s[0] not in {'1', '2'}:
            return 0
        elif s[1] == '0' and s[0] in {'1', '2'}:
            dp[1] = 1
        elif int(s[:2]) > 26:
            dp[1] = 1
        else:
            dp[1] = 2
        for i in range(2, len(s)):
            if s[i] == '0' and s[i-1] not in {'1', '2'}:
                return 0
            elif s[i] == '0' and s[i-1] in {'1', '2'}:
                dp[i] = dp[i-2]
            elif int(s[i-1:i+1]) > 26 or s[i-1] == '0':
                dp[i] = dp[i-1]
            else:
                dp[i] = dp[i-1] + dp[i-2]
            print(dp)
        return dp[-1]


class Solution2():
    def main(self, s:str):
        if s[0] == "0":
            return 0
        dp = [1 for _ in s]
        for i in range(1, len(s)):
            if s[i] == '0':
                if int(s[i-1:i+1]) > 26:
                    return 0
                else:
                    dp[i] = dp[i-2]
            else:
                if int(s[i-1:i+1]) > 26 or s[i-1] == "0":
                    dp[i] = dp[i-1]
                else:
                    if i != 1:
                        dp[i] = dp[i-1] + dp[i-2]
                    else:
                        dp[i] = 2

        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    print(s.numDecodings('226'))
    s2 = Solution2()
    print(s2.main('226'))
