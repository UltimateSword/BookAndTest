def is_match(s, p) -> bool:
    if not p:
        return not s
    if not s:
        for i in p:
            if i != "*":
                return False
        return True
    first = p[0] in {s[0], '?', '*'}
    if p[0] == '*' and len(p) < 2:
        return first
    elif p[0] == '*' and len(p) >= 2:
        for i in range(len(s)):
            if is_match(s[i:], p[1:]):
                return True
        return False
    elif first:
        return is_match(s[1:], p[1:])
    else:
        return False


def dp_match(s: str, p: str) -> bool:
    dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
    dp[0][0] = True
    for i in range(1, len(p)+1):
        if p[i-1] == "*" and dp[0][i-1]:
            dp[0][i] = True
    for i in range(1, len(s) + 1):
        for j in range(1, len(p) + 1):
            if (s[i - 1] == p[j - 1] or p[j-1] == '?') and dp[i-1][j-1]:
                dp[i][j] = True
            elif p[j - 1] == '*' and (dp[i][j - 1] or dp[i - 1][j]):  # 关键是这一步
                dp[i][j] = True
    return dp[len(s)][len(p)]


if __name__ == "__main__":
    print(dp_match('aa', '*'))