"""
For strings S and T, we say "T divides S" if and only if S = T + ... + T  (T concatenated with itself 1 or more times)

Return the largest string X such that X divides str1 and X divides str2.

 

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""
 

Note:

1 <= str1.length <= 1000
1 <= str2.length <= 1000
str1[i] and str2[i] are English uppercase letters.


链接：https://leetcode-cn.com/problems/greatest-common-divisor-of-strings

"""


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) > len(str2):  # str1:shorter str2;longer
            str1, str2 = str2, str1
        i = 1
        T1 = ''
        while i < len(str1) - 1:
            if not T1 and str1[:i] == str1[i:i+i]:
                T1 = str1[:i]
                i += i
            elif str1[i:i+len(T1)] == T1 and T1:
                i += len(T1)
            else:
                T1 = ''
                i += 1
        if not T1:
            T1 = str1
        if len(str2) % len(T1):
            return ''
        if T1 * (len(str2) // len(T1)) != str2:
            return ''
        else:
            i = len(T1)
            ans = 1
            while i < len(str1)+1:
                if not len(str2) % i and not len(str1) % i:
                    ans = i // len(T1)
                i += 1
            return T1 * ans

    def gcdOfStrings_quicker(self, str1: str, str2: str) -> str:
        import math
        candicate = math.gcd(len(str1), len(str2))
        if str1[:candicate] * (len(str1) // candicate) != str1 or str1[:candicate] * (len(str1) // candicate) != str2:
            return ''
        return str1[:candicate]


if __name__ == '__main__':
    s = Solution()
    print(s.gcdOfStrings('ABC', 'ABCABC'))