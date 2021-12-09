from functools import reduce
from operator import mul

with open("input.txt", "r") as f:
    heights = [ [int(n) for n in c.strip()] for c in f.readlines()]

width = len(heights[0])
height = len(heights)

lows = []
for row in range(height):
    for col in range(width):
        val = heights[row][col]
        is_low = True
        for row_adj, col_adj in [(-1, 0), (1,0), (0,1), (0,-1)]:
            try:
                other = heights[row + row_adj][col + col_adj]
            except:
                continue
            if val >= other:
                is_low = False
                break
        if is_low:
            lows.append([row,col])

basin_sizes = []
for low in lows:
    basin = set()
    basin.add(tuple(low))
    q = [low]
    while len(q) > 0:
        row, col = q.pop(0)
        for row_adj, col_adj in [(-1, 0), (1,0), (0,1), (0,-1)]:
            r = row + row_adj
            c = col + col_adj
            if r == -1 or c == -1:
                continue
            try:
                other = heights[r][c]
            except:
                continue
            if other < 9 and tuple([r,c]) not in basin:
                basin.add(tuple([r,c]))
                q.append([r,c])

    basin_sizes.append(len(basin))

basin_sizes.sort()
print(reduce(mul, basin_sizes[-3:], 1))
                