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
    dp = [[False for _ in p] for _ in s]



if __name__ == '__main__':
    print(is_match("mississippi", "m??*ss*?i*pi"))
