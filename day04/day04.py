#!/usr/bin/env python3

from time import perf_counter as pfc


def read(path: str):
    with open(path) as my_file:
        drawn = [int(num) for num in my_file.readline().rstrip().split(',')]

        raw = [line.rstrip() for line in my_file.readlines()] 
        del raw[0]
        boards = []

        grid = []
        for row in raw:
            if row != '':
                grid.append([(int(num), False) for num in row.split()])
            else:
                boards.append(grid)
                grid = []
        boards.append(grid)

        return drawn, boards


def read2(path: str):
    """
    Reads the input without marking.
    This might be usefull later.
    """
    with open(path) as my_file:
        inp = my_file.read().rstrip()

        numbers = [int(num) for num in inp.splitlines()[0].split(',')]

        boards_raw = inp.split('\n\n')[1:]
        boards = [[[int(num) for num in row.split()] for row in board.split('\n')] for board in boards_raw]

        return numbers, boards


def check_win(grid: list):
    for i in range(len(grid)):
        horizontal = all([pair[1] for pair in grid[i]])

        column = []
        for j in range(len(grid)):
            column.append(grid[j][i])
        vertical = all([pair[1] for pair in column])

        if horizontal or vertical:
            return True

    return False


def solve1():
    drawn, boards = read('day04_input.txt')

    for num in drawn:
        for grid in boards:
            for row in grid:
                if (num, False) in row:
                    row[row.index((num, False))] = (num, True)

            if check_win(grid):
                sum_unmarked = 0
                for i in range(len(grid)):
                    sum_unmarked += sum([pair[0] for pair in grid[i] if not pair[1]])

                return num * sum_unmarked


def solve2():
    drawn, boards = read('day04_input.txt')

    winning = [(False, 0) for i in range(len(boards))]
    scores = []

    for num in drawn:
        for grid in boards:
            for row in grid:
                if (num, False) in row:
                    row[row.index((num, False))] = (num, True)

            if check_win(grid):
                sum_unmarked = 0
                for i in range(len(grid)):
                    sum_unmarked += sum([pair[0] for pair in grid[i] if not pair[1]])

                score = num * sum_unmarked

                if not winning[boards.index(grid)][0]:
                    winning[boards.index(grid)] = (True, score)
                    scores.append(score)

    return scores[len(scores)-1]


start = pfc()
print(solve1(), pfc()-start)

print()

start = pfc()
print(solve2(), pfc()-start)

