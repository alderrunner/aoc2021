#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from time import perf_counter as pfc
from functools import reduce


def read(path: str):
    with open(path) as my_file:
        return [[int(num) for num in line] for line in my_file.read().rstrip().split('\n')]


def is_low_point(i, j, inp):
    right = left = top = bottom = False

    if j+1 < len(inp[i]):
        right = inp[i][j] < inp[i][j+1]
    else:
        right = True

    if j-1 >= 0:
        left = inp[i][j] < inp[i][j-1]
    else:
        left = True

    if i+1 < len(inp):
        bottom = inp[i][j] < inp[i+1][j]
    else:
        bottom = True

    if i-1 >= 0:
        top = inp[i][j] < inp[i-1][j]
    else:
        top = True

    return right and left and top and bottom


def solve1(inp):
    risk_level = []

    for i in range(len(inp)):
        for j in range(len(inp[i])):
            if is_low_point(i, j, inp):
                risk_level.append(inp[i][j]+1)

    return sum(risk_level)


def get_basin_size(i, j, inp):
    visited = []
    queue = []
    size = 0

    queue.append((i, j))

    while queue:
        (i, j) = queue.pop(0)

        if (i, j) in visited:
            continue

        visited.append((i, j))
        size += 1

        if j+1 < len(inp[i]) and inp[i][j+1] != 9:
            queue.append((i, j+1))

        if j-1 >= 0 and inp[i][j-1] != 9:
            queue.append((i, j-1))

        if i+1 < len(inp) and inp[i+1][j] != 9:
            queue.append((i+1, j))

        if i-1 >= 0 and inp[i-1][j] != 9:
            queue.append((i-1, j))
        
    return size


def solve2(inp):
    low_points = []

    for i in range(len(inp)):
        for j in range(len(inp[i])):
            if is_low_point(i, j, inp):
                low_points.append((i, j))

    three_largest_basins = [0, 0, 0]
    
    for i, j in low_points:
        basin_size = get_basin_size(i, j, inp)

        if basin_size > min(three_largest_basins):
            three_largest_basins.remove(min(three_largest_basins))
            three_largest_basins.append(basin_size)

    return reduce((lambda x, y: x*y), three_largest_basins)


path = "day09/day09_input.txt"
inp1 = read(path)
inp2 = read(path)

start = pfc()
print(f"The solution to part 1 is: {solve1(inp1)} in {pfc() - start} seconds")

start = pfc()
print(f"The solution to part 2 is: {solve2(inp2)} in {pfc() - start} seconds")
