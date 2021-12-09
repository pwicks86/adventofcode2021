with open("input.txt", "r") as f:
    crabs = list(map(int, f.read().split(",")))

min_pos = min(crabs)
max_pos = max(crabs)

diff_sums = []
for pos in range(min_pos, max_pos):
    diff_list = [abs(c - pos) for c in crabs]
    diff_sums.append(sum(diff_list))

print(min(diff_sums))

