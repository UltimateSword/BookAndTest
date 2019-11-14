def find_max_palindrome(s):
    """
    动态规划：查找最大回文子川
    1. 找到状态 p = [m*m]
    2. 找到状态转换方程，找到循环不变式
    p[l][r]状态取决于p[l+1]p[r-1] 和 s[l] s[r]
    因此从长度为1的字符串可以推导出长度为n的字符串状态。
    3. 注意事项：list是左闭右开的。
    :param s: 字符串
    :return:
    """
    length = len(s)
    dp = [[False for _ in range(length)] for _ in range(length)]
    res = ''
    for r in range(length):
        for l in range(r):
            dp[l][r] = s[l] == s[r] and (r-l <= 2 or dp[l + 1][r - 1])
            if dp[l][r]:
                if r + 1 - l > len(res):
                    res = s[l:r+1]
    return res


if __name__ == '__main__':
    print(find_max_palindrome('cabac'))
