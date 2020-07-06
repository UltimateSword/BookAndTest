"""
Find the length of the longest substring T of a given string (consists of lowercase letters only) such that every character in T appears no less than k times.

Example 1:

Input:
s = "aaabb", k = 3

Output:
3

The longest substring is "aaa", as 'a' is repeated 3 times.
Example 2:

Input:
s = "ababbc", k = 2

Output:
5

The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.


链接：https://leetcode-cn.com/problems/longest-substring-with-at-least-k-repeating-characters

"""


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        from collections import Counter

        def cnt(l: int, r: int) -> int:
            count_s = Counter(s[l:r+1])
            while l <= r and count_s[s[l]] < k:  # 减去左侧肯定不满足的字符
                l += 1
            while l <= r and count_s[s[r]] < k:  # 减去右侧肯定不满足的字符
                r -= 1
            if r - l + 1 < k:  # 最终有可能还是不行
                return 0
            partial = l
            while partial <= r and count_s[s[partial]] >= k:
                partial += 1
            if partial >= r:
                return r - l + 1
            print(partial, l, r)
            return max(cnt(l, partial-1), cnt(partial+1, r))
        return cnt(0, len(s)-1)

    def longestSubstring_quicker(self, s: str, k: int) -> int:
        for i in set(s):
            if s.count(i) < k:
                return max([self.longestSubstring(j, k) for j in s.split(i)])
        return len(s)


class Solution1(object):
    def find(self, s, k):
        for i in s:
            if s.count(i) < k:
                return max([self.find(one, k) for one in s.split(i)])
        return len(s)


if __name__ == '__main__':
    s = Solution()
    print(s.longestSubstring("aaabbb", 3))