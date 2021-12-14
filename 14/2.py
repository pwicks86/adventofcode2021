from collections import Counter
from collections import defaultdict

with open("input.txt", "r") as f:
    stuff = f.read()

start, rulestr = stuff.split("\n\n")
rules = {}
for rule in rulestr.splitlines():
    a, b = rule.split(" -> ")
    rules[a] = b

class State:
    def __init__(self):
        self.pairs = defaultdict(int)
        self.counts = Counter()

    def step(self):
        new_pairs = defaultdict(int)
        for pair, count in self.pairs.items():
            if pair in rules:
                new_pairs[pair[0] + rules[pair]] += count  
                new_pairs[rules[pair] + pair[1]] += count  
                self.counts[rules[pair]] += count
            else:
                new_pairs[pair] = count
        self.pairs = new_pairs

state = defaultdict(int)
for i in range(len(start) - 1):
    state[start[i:i+2]] += 1

ss = State()
ss.pairs = state
ss.counts = Counter(start)
for i in range(40):
    ss.step()
common = ss.counts.most_common()
print(common[0][1] - common[-1][1])