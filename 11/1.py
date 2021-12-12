from copy import deepcopy
# with open("test.txt", "r") as f:
with open("input.txt", "r") as f:
    lines = f.readlines()

def print_state(state):
    for row in state:
        print("".join(map(str,row)))
    print()

num_rows = len(lines)
num_cols = len(lines[0]) - 1
octo = []
for l in lines:
    o = []
    for c in l:
        try:
            o.append(int(c))
        except:
            pass
    octo.append(o)

# print_state(octo)
flash_count = 0

def do_step(state):
    global flash_count
    new_state = deepcopy(state)
    # step 1
    for row in range(num_rows):
        for col in range(num_cols):
            new_state[row][col] += 1
            if new_state[row][col] == 10:
                new_state[row][col] = "x"

    # step 2

    while True:
        flashing = False
        for row in range(num_rows):
            for col in range(num_cols):
                if new_state[row][col] == "x":
                    new_state[row][col] = "o"
                    flash_count += 1
                    flashing = True
                    for row_adj in [-1, 0, 1]:
                        for col_adj in [-1, 0, 1]:
                            if row_adj == 0 and col_adj == 0:
                                continue
                            try:
                                if row + row_adj == -1 or col + col_adj == -1:
                                    continue
                                cur_val = new_state[row + row_adj][col + col_adj]
                                if cur_val not in ["x", "o"]:
                                    new_state[row + row_adj][col + col_adj] += 1
                                    if new_state[row + row_adj][col + col_adj] == 10:
                                        new_state[row + row_adj][col + col_adj] = "x"
                            except:
                                pass
        if not flashing:
            break
    
    # step 3
    for row in range(num_rows):
        for col in range(num_cols):
            if new_state[row][col] == "o":
                new_state[row][col] = 0

    return new_state


for i in range(100):
    octo = do_step(octo)

print(flash_count)

    