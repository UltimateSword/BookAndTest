class Solution:
    def longestCommonPrefix(self, strs: list) -> str:
        i = 0
        result = []
        status = True
        while status:
            if len(strs[0]) > i:
                one = strs[0][i]
            else:
                break
            for j in strs:
                if i >= len(j):
                    status = False
                    break
                elif j[i] != one:
                    status = False
                    break
            if status:
                result.append(one)
            i += 1
        return ''.join(result)


if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonPrefix(['flow', 'fl', 'floee']))