#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from time import perf_counter as pfc


def read(path: str):
    with open(path) as my_file:
        part = my_file.read().rstrip().split('\n\n')
        data = [(int(point[:point.index(',')]),int(point[point.index(',')+1:])) for point in part[0].splitlines()]
        instructions = [(line[line.index('=')-1],int(line[line.index('=')+1:])) for line in part[1].splitlines()]
        return data, instructions


def split_y(grid, pos):
    # Horizontal
    a = grid[:pos]
    b_temp = grid[pos+1::]
    b = b_temp[::-1]

    for i, line in enumerate(a):
        for j, mark in enumerate(line):
            a[i][j] = mark or b[i][j]
    
    return a


def split_x(grid, pos):
    # Vertical
    a = []
    b = []

    for row in grid:
        a.append(row[:pos])
        b_temp = row[pos+1:]
        b.append(b_temp[::-1])
    
    for i, line in enumerate(a):
        for j, mark in enumerate(line):
            a[i][j] = mark or b[i][j]
    
    return a


def solve1(inp):
    points = inp[0]
    instructions = inp[1]

    max_x = max_y = 0

    for point in points:
        if point[0] > max_x:
            max_x = point[0]
        
        if point[1] > max_y:
            max_y = point[1]
    
    grid = []
    row = [False]*(max_x+1)
    for _ in range(max_y+1):
        grid.append(row.copy())
    
    for x, y in points:
        grid[y][x] = True
    
    match instructions[0][0]:
        case 'x':
            grid = split_x(grid, instructions[0][1])
        case 'y':
            grid = split_y(grid, instructions[0][1])
    
    return sum(row.count(True) for row in grid)


def solve2(inp):
    points = inp[0]
    instructions = inp[1]

    max_x = max_y = 0

    for point in points:
        if point[0] > max_x:
            max_x = point[0]
        
        if point[1] > max_y:
            max_y = point[1]
    
    if max_x % 2 == 1:
        max_x += 1
    
    if max_y % 2 == 1:
        max_y += 1
    
    grid = []
    row = [False]*(max_x+1)
    for _ in range(max_y+1):
        grid.append(row.copy())
    
    for x, y in points:
        grid[y][x] = True
    
    for i, _ in enumerate(instructions):
        match instructions[i][0]:
            case 'x':
                grid = split_x(grid, instructions[i][1])
            case 'y':
                grid = split_y(grid, instructions[i][1])
    
    for i, row in enumerate(grid):
        for j, mark in enumerate(row):
            if mark:
                grid[i][j] = '#'
            else:
                grid[i][j] = '.'
    
    for row in grid:
        print(row)
    
    return 'HECRZKPR'


path = "day13/day13_input.txt"
inp1 = read(path)
inp2 = read(path)

start = pfc()
print(f"The solution to part 1 is: {solve1(inp1)} in {pfc() - start} seconds")

start = pfc()
print(f"The solution to part 2 is: {solve2(inp2)} in {pfc() - start} seconds")
