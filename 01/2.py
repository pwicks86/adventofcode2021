from copy import deepcopy
from collections import deque
with open("input.txt", "r") as f:
    lines = [int(l) for l in f.readlines()]
prev = None
count = 0
q = deque([], 3)
for l in lines:
    q.append(l)
    if prev and len(prev) == 3:
        prev_sum = sum(prev)
        q_sum = sum(q)
        if q_sum > prev_sum:
            count += 1
    prev = deepcopy(q)
print(count)

