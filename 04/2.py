import sys
with open("input.txt", "r") as f:
    puz = f.read()

blocks = puz.split("\n\n")

def mk_2d(r,c):
    arr = []
    for _ in range(r):
        arr.append([0] * c)
    return arr


nums = [int(i) for i in blocks.pop(0).split(",")]
boards = []
nrows = 5
ncols = 5
for b in blocks:
    arr = []
    rows = b.split("\n")
    for ri, row in enumerate(rows):
        row_arr = []
        for ci, i in enumerate(row.split()):
            row_arr.append(int(i))
        arr.append(row_arr)
    boards.append(arr)

guesses = []
for i in range(len(boards)):
    guesses.append(mk_2d(ncols,nrows))

def check_winner(board_num):
    row_totals = [ sum(x) for x in guesses[board_num] ]
    col_totals = [ sum(x) for x in zip(*guesses[board_num])]
    return 5 in row_totals or 5 in col_totals

def check_final_score(board_num, last_num):
    n = []
    for row in range(nrows):
        for col in range(ncols):
            if guesses[board_num][row][col] == 0:
                n.append(boards[board_num][row][col])
    return sum(n) * last_num
    

won_boards = set()
for num in nums:
    for board_num, board in enumerate(boards):
        for row in range(nrows):
            for col in range(ncols):
                if board[row][col] == num:
                    guesses[board_num][row][col] = 1
        if check_winner(board_num):
            won_boards.add(board_num)
        if len(won_boards) == len(boards):
            # then we won, calculate final score
            print(check_final_score(board_num, num))
            sys.exit(0)

