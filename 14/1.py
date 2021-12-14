from collections import Counter
# with open("test.txt", "r") as f:
with open("input.txt", "r") as f:
    stuff = f.read()

start, rulestr = stuff.split("\n\n")
rules = {}
for rule in rulestr.splitlines():
    a, b = rule.split(" -> ")
    rules[a] = b

print(rules)

def step(start):
    end = ""
    i = 0
    while True:
        if i == len(start) - 1:
            break
        end += start[i]
        if start[i:i + 2] in rules:
            end += rules[start[i:i + 2]]
        i += 1
        #     i += 2
        # else:
        #     end += start[i]
        #     i += 1
    end += start[-1]
    return end

state = start
for _ in range(10):
    state = step(state)
print(len(state))
c = Counter(state)
common = c.most_common()
print(common[0][1] - common[-1][1])