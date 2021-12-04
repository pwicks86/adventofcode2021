from collections import defaultdict
with open("input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

sums = defaultdict(int)
for l in lines:
    for idx, c in enumerate(l):
        sums[idx] += int(c)
gamma_str = ""
epsilon_str = ""
for k,v in sums.items():
    gbit = "1" if float(v) / len(lines) > 0.5 else "0"
    gamma_str += gbit
    ebit = "0" if float(v) / len(lines) > 0.5 else "1"
    epsilon_str += ebit

gamma = int(gamma_str, 2)
epsilon = int(epsilon_str, 2)
print(gamma * epsilon)
