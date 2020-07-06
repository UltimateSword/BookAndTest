nums = [int(i) for i in input().split()]
nums.sort()
a, b = 0, 0
from collections import Counter


def is_valid(l:list):
    l.sort()
    c = Counter(l)
    c2s = [a for a, b in c.items() if b >= 2]