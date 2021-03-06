"""
Implement a method to perform basic string compression using the counts of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the "compressed" string would not become smaller than the original string, your method should return the original string. You can assume the string has only uppercase and lowercase letters (a - z).

Example 1:

Input: "aabcccccaaa"
Output: "a2b1c5a3"
Example 2:

Input: "abbccd"
Output: "abbccd"
Explanation:
The compressed string is "a1b2c2d1", which is longer than the original string.


链接：https://leetcode-cn.com/problems/compress-string-lcci

"""


class Solution:
    def compressString(self, S: str) -> str:
        ans = S[0]
        last = 1
        for i in range(1, len(S)):
            if S[i] == S[i-1]:
                last += 1
            else:
                ans = ''.join([ans, str(last), S[i]])
                last = 1
        ans = ''.join([ans, str(last)])
        return ans if len(ans) < len(S) else S


if __name__ == '__main__':
    s = Solution()
    print(s.compressString('a'))