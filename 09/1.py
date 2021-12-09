with open("input.txt", "r") as f:
    heights = [ [int(n) for n in c.strip()] for c in f.readlines()]

width = len(heights[0])
height = len(heights)

total_risk = 0
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
            risk_level = val + 1
            total_risk += risk_level

print(total_risk)
                