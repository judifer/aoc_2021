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
    for i in numbers:
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
                for col in range(0, len(board)):
                    x = 0
                    for line in board:
                        if line[col] == None:
                            x += 1
                    if x == 5:
                        winners.add(idx)
                        if len(winners) == 1:
                            first = summer(board, i)
                if len(winners) == len(boards):
                    second = summer(board, i)
                    return first, second

a, b = bingo(numbers, boards)
print(f"Part one: {a}")
print(f"Part two: {b}")