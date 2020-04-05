"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 队列法 先进队列 在拼凑字符串 再吐出来
class Solution:
    def letterCombinations(self, digits: str) -> list:
        # a-z: 97-122, 2-9:50-57
        # 2: [97, 100] [97+0, 97+3]
        # 3: [100, 103] [97+3, 97+6]
        if not digits: return []
        trans = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        res = ['']
        for d in digits:
            for _ in range(len(res)):
                tmp = res.pop(0)
                for j in trans[ord(d) - 50]:
                    # print(tmp, j, trans(ord(d)))
                    res.append(tmp + j)
        return res


# 回溯法: 递归 py缺点无尾递归优化 容易打满内存
class Recall(object):
    def letterCombinations(self, digits: str) -> list:
        if not digits:
            return []
        trans = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        tmp = ''
        res = []
        def recall(tmp, new_digits):
            if not new_digits:
                return
            for i in trans[ord(new_digits[0]) - 50]:
                recall(tmp+i, new_digits[1:])
            if len(new_digits) == 1:
                for i in trans[ord(new_digits) -50]:
                    res.append(tmp+i)
        recall(tmp, new_digits=digits)
        return res




if __name__ == '__main__':
    S = Recall()
    print(S.letterCombinations('23'))