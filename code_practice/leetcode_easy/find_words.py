"""
You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.

 

Example 1:

Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation:
The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
Example 2:

Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation:
The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.
 

Note:

1 <= words.length <= 1000
1 <= words[i].length, chars.length <= 100
All strings contain lowercase English letters only.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-words-that-can-be-formed-by-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def countCharacters(self, words: list, chars: str) -> int:
        from collections import Counter
        count_char = Counter(chars)
        ans = 0
        for word in words:
            count_one = Counter(word)
            one = 0
            for i in count_one:
                if count_char.get(i, 0) < count_one[i]:
                    one = 0
                    break
                else:
                    one += count_one[i]
            ans += one
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.countCharacters(words = ["hello","world","leetcode"], chars = "welldonehoneyr"))