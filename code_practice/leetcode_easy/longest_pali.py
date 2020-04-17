"""
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
"""


class Solution(object):
    def max_length_palindrome(self, s: str) -> int:
        from collections import Counter
        count_s = Counter(s)
        ans = 0
        plus = 0
        for i in count_s.values():
            if not i % 2:
                ans += i
            else:
                plus = 1
                ans += i-1
        return ans + plus


if __name__ == '__main__':
    s = Solution()
    print(s.max_length_palindrome('ccccdd'))