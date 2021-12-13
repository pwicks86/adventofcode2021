with open("input.txt", "r") as f:
    i = f.read()

points, folds = i.split("\n\n")
points =[tuple(map(int,p.split(","))) for p in points.splitlines()]

folds = [(f[11], int(f[13:])) for f in folds.splitlines()]
field = set()
for p in points:
    field.add(p)

def fold(f, axis, line):
    new_f = set()
    for x, y in f:
        if axis == "y":
            if y > line:
                dist = abs(y - line)
                new_f.add((x, y - (2*dist)))
            else:
                new_f.add((x,y))
        else:
            if x > line:
                dist = abs(x - line)
                new_f.add((x - (2*dist), y))
            else:
                new_f.add((x,y))
    return new_f


for f in folds:
    field = fold(field, f[0], f[1])

max_x = 0
max_y = 0
for f in field:
    x,y = f
    max_x = max(max_x, x)
    max_y = max(max_y, y)

for row in range(max_y + 1):
    for col in range(max_x + 1):
        if (col, row) in field:
            print("0", end="")
        else:
            print(".", end="")
    print()
