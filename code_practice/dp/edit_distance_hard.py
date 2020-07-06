"""
Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')


链接：https://leetcode-cn.com/problems/edit-distance

"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if not word2 or not word1:
            return len(word1) + len(word2)
        dp = [[0] * (len(word2)+1) for _ in range(len(word1)+1)]
        # dp[0][j]=j,
        for i in range(len(word1)+1):
            for j in range(len(word2)+1):
                if i == 0:
                    dp[0][j] = j
                elif j == 0:
                    dp[i][0] = i
                else:
                    left = dp[i-1][j] + 1
                    up = dp[i][j-1] + 1
                    if word1[i-1] == word2[j-1]:
                        dp[i][j] = min(dp[i-1][j-1], left, up)
                    else:
                        dp[i][j] = min(dp[i-1][j-1] + 1, left, up)
        return dp[-1][-1]


class Solution2(object):
    def main(self, word1, word2):
        # easy: "" ""
        if word1 == word2:
            return 0
        m, n = len(word1), len(word2)
        dp = [[0] * m for _ in range(n)]





if __name__ == '__main__':
    s = Solution()
    print(s.minDistance(word1="horse", word2="ros"))