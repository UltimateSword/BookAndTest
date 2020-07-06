# a, b = [int(i) for i in input().split()]
# nums = [int(i) for i in input().split()]
b = 19
res = 0
def recall(cur, candidates):
    global res
    if len(cur) == 3:
        res += 1
        return
    n = len(candidates)
    for i in range(n):
        new = candidates.pop()
        if cur == [] or cur[0] - new <= b:
            cur.append(new)
            recall(cur, [i for i in candidates])
            cur.pop()

recall([], [1, 10, 20, 30, 50])
# recall([], [1, 2,3,4])
print(res)