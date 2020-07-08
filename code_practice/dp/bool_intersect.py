class Solution():
    def main(self, s1, s2, s3):
        m, n = len(s1) + 1, len(s2) + 1
        dp = [[False] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[0][0] = True
                elif i == 0:
                    dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]
                elif j == 0:
                    dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]
                else:
                    left = s3[i + j - 1] == s2[j - 1] and dp[i][j - 1]
                    right = s3[i + j - 1] == s1[i - 1] and dp[i - 1][j]
                    dp[i][j] = left or right
        return dp[-1][-1]