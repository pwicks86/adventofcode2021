with open("input.txt", "r") as f:
    ints = f.readlines()
h = 0
d = 0
for i in ints:
    op, val = i.split()
    val = int(val)
    if op == "forward":
        h += val
    elif op == "down":
        d += val
    else:
        d -= val
print(h*d)

