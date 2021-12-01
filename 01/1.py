with open("input.txt", "r") as f:
    lines = [int(l) for l in f.readlines()]
prev = None
count = 0
for l in lines:
    if prev:
        if l > prev:
            count += 1
    prev = l
print(count)

