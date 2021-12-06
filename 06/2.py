from collections import defaultdict
with open("input.txt", "r") as f:
    fish = list(map(int, f.read().split(",")))

fish_dict = defaultdict(int)
for f in fish:
    fish_dict[f] += 1


def step(fish_d):
    new_d = defaultdict(int)
    for day in fish_d.keys():
        step_day = day - 1
        if step_day < 0:
            new_d[6] += fish_d[day]
            new_d[8] = fish_d[day]
        else:
            new_d[day - 1] += fish_d[day]
    return new_d

for i in range(256):
    fish_dict = step(fish_dict)

print(sum(fish_dict.values()))