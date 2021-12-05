from collections import defaultdict
with open("input.txt", "r") as f:
    lines = f.readlines()

segs = []
max_val = -1 
for line in lines:
    a, b = line.strip().split(" -> ")
    x1, y1 = map(int, a.split(","))
    x2, y2 = map(int, b.split(","))
    max_val = max(x1, x2, y1, y2, max_val)
    segs.append([[x1, y1], [x2,y2]])

floor = defaultdict(int)
for seg in segs:
    if seg[0][0] == seg[1][0]:
        l = sorted([seg[0][1], seg[1][1]])
        for y in range(l[0], l[1] + 1):
            floor[(seg[0][0], y)] += 1 
    elif seg[0][1] == seg[1][1]:
        l = sorted([seg[0][0], seg[1][0]])
        for x in range(l[0], l[1] + 1):
            floor[(x, seg[0][1])] += 1 
    else:
        slope = float(seg[1][1] - seg[0][1]) / (seg[1][0] - seg[0][0])
        if slope == 1:
            cur = (seg[0][0], seg[0][1])
            end = (seg[1][0], seg[1][1])
            if cur > end:
                end, cur = cur, end
            while(True):
                floor[cur] +=1 
                if cur == end:
                    break
                cur = tuple(map(lambda x: x + 1, cur))
        elif slope == -1:
            cur = (seg[0][0], seg[0][1])
            end = (seg[1][0], seg[1][1])
            if cur > end:
                end, cur = cur, end
            while(True):
                floor[cur] +=1 
                if cur == end:
                    break
                cur = (cur[0] + 1, cur[1] - 1)

print(len([v for v in floor.values() if v >= 2]))

