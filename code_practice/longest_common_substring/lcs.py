def solution(s1, s2) -> int:
    len_lcs = 0
    for i in range(len(s1)):
        for j in range(len(s2)):
            ptr = 0
            while (i+ptr < len(s1)) and (j+ptr < len(s2)) and s1[i+ptr] == s2[j+ptr]:
                if ptr > len_lcs:
                    len_lcs = ptr
                ptr += 1
            if ptr > len_lcs:
                len_lcs = ptr
    return len_lcs


def df_solution(s1, s2):
    """
    字符串型
    A[i-1] B[j-1]
    if A[i]B[j] ? +1 : +0
    acde abcde
    """
    dp = [[0 for _ in range(len(s2))] for _ in range(len(s1))]
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                dp[i][j] += dp[i-1][j-1] + 1
    return max(map(lambda x: max(x), dp))



if __name__ == "__main__":
    print(solution('abcd', 'adbc'))
    print(df_solution('abcd', 'adbcdced'))
