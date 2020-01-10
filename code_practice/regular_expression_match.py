class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        s_len = len(s)
        p_len = len(p)
        dp = [[False for i in range(s_len)] for j in range(p_len)]
        for i in range(s_len):
            for j in range(p_len):
                if s[i] == s[j] and (dp[i-1][j-1] or i < 1 or j < 1):
                    dp[i][j] = True


