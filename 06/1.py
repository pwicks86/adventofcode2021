with open("input.txt", "r") as f:
    fish = list(map(int, f.read().split(",")))

def step(fish_list):
    out_fish = []
    new_fish = []
    for fish in fish_list:
        next_fish = fish - 1
        if next_fish < 0:
            next_fish = 6
            new_fish.append(8)
        out_fish.append(next_fish)
    out_fish.extend(new_fish)
    return out_fish

for i in range(80):
    fish = step(fish)
    # print(fish)

print(len(fish))