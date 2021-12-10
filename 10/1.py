with open("input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

paren_map = {
    "}":"{",
    "]":"[",
    ">":"<",
    ")":"(",
}

score_map = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
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
    return False, None

score = 0
for line in lines:
    borked, char = check_line(line)
    if borked:
        score += score_map[char]
print(score)

            

