with open("input.txt", "r") as f:
    ints = f.readlines()
h = 0
d = 0
a = 0
for i in ints:
    op, val = i.split()
    val = int(val)
    if op == "forward":
        h += val
        d += a * val
    elif op == "down":
        a += val
    else:
        a -= val
print(h*d)

