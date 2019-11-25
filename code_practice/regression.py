def is_match(s, p) -> bool:
    if not p:  # case:''
        return not s
    first = s and p[0] in {s[0], '.'}  # case: 1
    if len(p) >= 2 and p[1] == '*':  # case: >=2
        return is_match(s, p[2:]) or first and is_match(s[1:], p)
        # abc, first: a*bc, is_match(s,p[2:]), first: b*abc
    else:
        return first and is_match(s[1:], p[1:])