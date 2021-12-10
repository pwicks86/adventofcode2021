with open("input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

paren_map = {
    "}":"{",
    "]":"[",
    ">":"<",
    ")":"(",
}

paren_map2 = {
   "{":"}",
   "[":"]",
   "<":">",
   "(":")",
}

score_map = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}

def check_line(line):
    stack = []
    for c in line:
        if c in ["[","(","{","<"]:
            stack.append(c)
        else:
            most_recent = stack[-1]
            if paren_map[c] != most_recent:
                return True, c
            else:
                stack.pop()
    return False, stack

scores = []
for line in lines:
    borked, char = check_line(line)
    if borked:
        continue
    else:
        fix = []
        for c in reversed(char):
            fix.append(paren_map2[c])
        score = 0
        for c in fix:
            score = score * 5
            score += score_map[c]
        scores.append(score)

scores.sort()
middle = int((len(scores) - 1)/2)
print(scores[middle])

            

