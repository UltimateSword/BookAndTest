pm, coder, idea = [2, 2, 5]
text = """1 1 1 2
1 2 1 1
1 3 2 2
2 1 1 2
2 3 5 5"""
from collections import deque

queue = []
for t in text.split():
    queue = [[int(i) for i in t.split()]]
workers = [0] * coder
starts = sorted([j for j in set([i[1] for i in queue])])
for start in starts:
    first = filter(lambda x: workers[0] <= x[1] < start, queue)
