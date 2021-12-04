import math
from collections import defaultdict
with open("input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]
lines = [l for l in lines if len(l) > 0]
original_lines = lines

def round_half_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n*multiplier + 0.5) / multiplier

def round_half_down(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n*multiplier - 0.5) / multiplier

def get_sums(ll):
    sums = defaultdict(int)
    for l in ll:
        for idx, c in enumerate(l):
            sums[idx] += int(c)
    return sums

for pos in range(len(lines[0])):
    if len(lines) == 1:
        break
    sums = get_sums(lines)
    wanted_num = int(round_half_up(sums[pos] / len(lines)))
    lines = [l for l in lines if l[pos] == str(wanted_num)]

ox_gen = lines[0]
lines = original_lines
for pos in range(len(lines[0])):
    if len(lines) == 1:
        break
    sums = get_sums(lines)
    wanted_num = round_half_up(sums[pos] / len(lines))
    wanted_num = 1 if wanted_num == 0 else 0
    lines = [l for l in lines if l[pos] == str(wanted_num)]
co2_scrubber = lines[0]

print(int(ox_gen,2) * int(co2_scrubber,2))

