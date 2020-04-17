def solution(s1, s2) -> bool:
    len1, len2 = len(s1), len(s2)
    if len2 > len1:
        return False
    judge = dict()
    for i in range(len1):
        judge[s1[i]] = judge.get(s1[i], 0) + 1
        if i < len2:
            judge[s2[i]] = judge.get(s2[i], 0) - 1
    for i in judge:
        if judge[i] == -1:
            return False
    else:
        return True


if __name__ == '__main__':
    print(solution('abdcde', 'cde'))
