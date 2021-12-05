import sys

with open("day4.txt") as f:
    data = f.read().split('\n\n')

numbers = list(map(int, data[0].split(',')))
boards = [[list(map(int, l.split())) for l in board.split('\n')] for board in data[1:]]

def summer(x, number):
    winner = 0
    for line in x:
        for num in line:
            if num != None:
                winner += num
    return winner * number

def bingo(numbers, boards):
    winners = set()
    img = 0
    print_boards(boards, img)
    for i in numbers:
        temp_boards = [x for x in boards]
        img += 1
        for idx, board in enumerate(boards):
            if idx not in winners:
                for line in board:
                    for num in range(0, len(line)):
                        if line[num] == i:
                            line[num] = None
                for line in board:
                    x = 0
                    for num in line:
                        if num == None:
                            x += 1
                    if x == 5:
                        winners.add(idx)
                        if len(winners) == 1:
                            first = summer(board, i)
                        prep_winners(board, winners)
                for col in range(0, len(board)):
                    x = 0
                    for line in board:
                        if line[col] == None:
                            x += 1
                    if x == 5:
                        winners.add(idx)
                        if len(winners) == 1:
                            first = summer(board, i)
                        prep_winners(board, winners)
                if len(winners) == len(boards):
                    second = summer(board, i)
            print_boards(boards, img)
            if len(winners) == len(boards):
                return

def print_boards(org_boards, img):
    stdout = sys.stdout
    with open(f"img/img{img:03d}.txt", "w") as f:
        sys.stdout = f
        if len(org_boards) != 100:
            return
        if img > 0:
            print(f"{' ' * 96}Checking no {numbers[img - 1]}\n")
        else:
            print(f"{' ' * 96}Initializing...\n")
        rows = 8
        columns = 13
        for row in range(rows):
            if row:
                print()
            for board_row in range(5):
                for column in range(columns):
                    index = row * columns + column
                    if index >= 100:
                        continue
                    if column:
                        print("  ", end='')
                    board = org_boards[index]
                    print_row(board[board_row])
                print()
    sys.stdout = stdout

def print_row(row):
    pos_cnt = 0
    for i in row:
        if i == None:
            pos_cnt += 1
    if pos_cnt == 5:
        show = ["B", "I", "N", "G", "O"]
    else:
        show = [
            " " if i is None else i
            for i
            in row
        ]
    print(f"{show[0]:>2} {show[1]:>2} {show[2]:>2} {show[3]:>2} {show[4]:>2}", end='')

def prep_winners(board, win):
    for i in range(0, 5):
        board[i] = [None] * 5
    return board

bingo(numbers, boards)