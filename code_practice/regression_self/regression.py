def is_match(s, p) -> bool:
    if not p:  # case:''
        return not s
    first = s and p[0] in {s[0], '.'}  # case: 1
    if len(p) >= 2 and p[1] == '*':  # case: >=2
        return is_match(s, p[2:]) or (first and is_match(s[1:], p))
        # abc, {a*bc, b*abc}, is_match(s,p[2:]):, first-true: a*abc,.*abc
        # aac, {a*c,a*bc,a*aac},
    else:
        return first and is_match(s[1:], p[1:])


if __name__ == '__main__':
    print(is_match('abc', 'a*bc'))