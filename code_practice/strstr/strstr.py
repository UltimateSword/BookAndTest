def solution(s1, s2) -> bool:
    if len(s1) != len(s2):
        return False

    judge = dict()
    for i in range(len(s1)):
        judge[s1[i]] = judge.get(s1[i], 0) + 1
        judge[s2[i]] = judge.get(s2[i], 0) - 1
    for i in judge:
        if judge[i] != 0:
            return False
    else:
        return True

if __name__ == '__main__':
    print(solution('abdcd', 'cdbae'))
