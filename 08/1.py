from collections import defaultdict
from dataclasses import dataclass
from itertools import combinations

# with open("test.txt", "r") as f:
with open("input.txt", "r") as f:
    lines = f.readlines()

@dataclass
class Disp:
    pats: list[str]
    outs: list[str]

d_list = []
for l in lines:
    pats, outs = l.split(" | ")
    d_list.append(Disp(pats.split(" "), outs.strip().split(" ")))

total_count = 0
for disp in d_list:
    solved = {}
    sigmap = {}
    # map number to things it contains
    sigsets = defaultdict(set)
    # map length to things it contains
    siglists = defaultdict(list)
    for p in disp.pats:
        # 1
        if len(p) == 2:
            sigsets[1].update(tuple(p))
        # 7
        elif len(p) == 3:
            sigsets[7].update(tuple(p))
        # 4
        elif len(p) == 4:
            sigsets[4].update(tuple(p))
        # 2 or 3 or 5
        elif len(p) == 5:
            siglists[5].append(set(tuple(p)))
        # 0 or 6 or 9
        elif len(p) == 6:
            siglists[6].append(set(tuple(p)))
        # 8
        elif len(p) == 7:
            sigsets[8].update(tuple(p))
    a = sigsets[7] - sigsets[1]
    solved["a"] = a
    # figure out the 1 difference in the 5 lists
    diff_lists = []
    for c in combinations(siglists[5], 2):
        diff = c[0] - c[1]
        diff_lists.append(c[0] ^ c[1])

    # grab the thing in diff_lists that is length 4, that must have been the
    # combination of 5 and 3 and thus will contain bcef, which we can use to
    # solve for g by subtracting it and  a and 4 from any of the len 5 pats
    sides = [d for d in diff_lists if len(d) == 4][0]
    g = siglists[5][0] - sides - a - sigsets[4]
    solved["g"] = g

    # solve for d by subtracting sides and a and g from anything in 5 lists
    d = siglists[5][0] - sides - a - g
    solved["d"] = d

    # we know enough to solve 3 as a whole
    sigsets[3] = sigsets[1].union(a, d,  g)

    # solve left side
    left_side = sigsets[8] - sigsets[3]

    # time to solve for e
    for p in siglists[6]:
        possible_e = left_side - p
        if len(possible_e) > 0:
            e = possible_e
            solved["e"] = e
            break
    # now we can solve for b
    b = left_side - e
    solved["b"] = b

    # and f
    for p in siglists[6]:
        possible_f = p - a - d - g - b - e
        if len(possible_f) == 1:
            f = possible_f
            solved["f"] = f
            break
    # and finally c
    c = sigsets[1] - f
    solved["c"] = c

    sigsets[0] = a.union(b,c,e,f,g)
    sigsets[2] = a.union(c,d,e,g)
    sigsets[5] = a.union(b,d,f,g)
    sigsets[6] = a.union(b,d,e,f,g)
    sigsets[9] = a.union(b,c,d,f,g)
    count = 0
    for o in disp.outs:
        if set(tuple(o)) == sigsets[1]:
            count += 1
        if set(tuple(o)) == sigsets[4]:
            count += 1
        if set(tuple(o)) == sigsets[7]:
            count += 1
        if set(tuple(o)) == sigsets[8]:
            count += 1
    total_count += count

print(total_count)