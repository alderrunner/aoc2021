#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from time import perf_counter as pfc


def read(path: str):
    with open(path) as my_file:
        raw = my_file.read().rstrip()
        return [[[int(num) for num in points.split(",")] for points in line.split(" -> ")] for line in raw.splitlines()]


def solve1():
    data = read("day05/day05_input.txt")

    diagram = [[0 for _ in range(1000)] for _ in range(1000)]
    points = 0

    for line in data:
        # For readability
        x1 = line[0][0]
        x2 = line[1][0]
        y1 = line[0][1]
        y2 = line[1][1]

        if (x1 != x2) and (y1 != y2):
            continue

        horizontal = None
        vertical = None
        q = 0

        if x1 < x2:
            horizontal = range(x1, x2 + 1)
            q = y1
        elif y1 < y2:
            vertical = range(y1, y2 + 1)
            q = x1
        elif x1 > x2:
            horizontal = range(x2, x1 + 1)
            q = y1
        elif y1 > y2:
            vertical = range(y2, y1 + 1)
            q = x1

        if horizontal:
            for i in horizontal:
                if diagram[q][i] == 1:
                    points += 1
                diagram[q][i] += 1

        if vertical:
            for i in vertical:
                if diagram[i][q] == 1:
                    points += 1
                diagram[i][q] += 1
    
    return points


def solve2():
    data = read("day05/day05_input.txt")

    diagram = [[0 for _ in range(1000)] for _ in range(1000)]
    points = 0

    for line in data:
        # For readability
        x1 = line[0][0]
        x2 = line[1][0]
        y1 = line[0][1]
        y2 = line[1][1]

        horizontal = None
        vertical = None
        q = 0

        diagonal = None

        if (x1 < x2) and (y1 == y2):
            horizontal = range(x1, x2 + 1)
            q = y1
        elif (y1 < y2) and (x1 == x2):
            vertical = range(y1, y2 + 1)
            q = x1
        elif (x1 > x2) and (y1 == y2):
            horizontal = range(x2, x1 + 1)
            q = y1
        elif (y1 > y2) and (x1 == x2):
            vertical = range(y2, y1 + 1)
            q = x1
        elif (x1 < x2) and (y1 < y2):
            xs = [i for i in range(x1, x2 + 1)]
            ys = [i for i in range(y1, y2 + 1)]

            diagonal = zip(xs, ys)
        elif (x1 < x2) and (y1 > y2):
            xs = [i for i in range(x1, x2 + 1)]
            ys = [i for i in range(y1, y2 - 1, -1)]

            diagonal = zip(xs, ys)
        elif (x1 > x2) and (y1 < y2):
            xs = [i for i in range(x2, x1 + 1)]
            ys = [i for i in range(y2, y1 - 1, -1)]

            diagonal = zip(xs, ys)
        elif (x1 > x2) and (y1 > y2):
            xs = [i for i in range(x2, x1 + 1)]
            ys = [i for i in range(y2, y1 + 1)]

            diagonal = zip(xs, ys)

        if horizontal:
            for i in horizontal:
                if diagram[q][i] == 1:
                    points += 1
                diagram[q][i] += 1

        if vertical:
            for i in vertical:
                if diagram[i][q] == 1:
                    points += 1
                diagram[i][q] += 1
        
        if diagonal:
            for i, j in diagonal:
                if diagram[j][i] == 1:
                    points += 1
                diagram[j][i] += 1

    return points


start = pfc()
print(f"The solution to part 1 is: {solve1()} in {pfc() - start} seconds")

start = pfc()
print(f"The solution to part 2 is: {solve2()} in {pfc() - start} seconds")
