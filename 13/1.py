# with open("input.txt", "r") as f:
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
    break

print(len(field))