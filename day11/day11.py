#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from time import perf_counter as pfc


def read(path: str):
    with open(path) as my_file:
        return [[int(num) for num in line] for line in my_file.read().rstrip().split("\n")]


def solve1(inp):
    flashes = 0

    for _ in range(1, 101):
        flash_pos = []

        for i, line in enumerate(inp):
            for j, num in enumerate(line):
                inp[i][j] += 1

                if num + 1 > 9:
                    flash_pos.append((i, j))
        
        already_flashed = []
        
        while flash_pos:
            flashes += 1
            i, j = flash_pos.pop(0)
            already_flashed.append((i,j))

            if i == 0:
                pass
            elif j == 0:
                inp[i-1][j] += 1
                if inp[i-1][j] > 9 and (i-1,j) not in already_flashed and (i-1,j) not in flash_pos:
                    flash_pos.append((i-1, j))

                inp[i-1][j+1] += 1
                if inp[i-1][j+1] > 9 and (i-1,j+1) not in already_flashed and (i-1,j+1) not in flash_pos:
                    flash_pos.append((i-1, j+1))
            elif j == len(inp[i])-1:
                inp[i-1][j] += 1
                if inp[i-1][j] > 9 and (i-1, j) not in already_flashed and (i-1, j) not in flash_pos:
                    flash_pos.append((i-1, j))

                inp[i-1][j-1] += 1
                if inp[i-1][j-1] > 9 and (i-1,j-1) not in already_flashed and (i-1,j-1) not in flash_pos:
                    flash_pos.append((i-1, j-1))
            else:
                inp[i-1][j] += 1
                if inp[i-1][j] > 9 and (i-1, j) not in already_flashed and (i-1, j) not in flash_pos:
                    flash_pos.append((i-1, j))

                inp[i-1][j-1] += 1
                if inp[i-1][j-1] > 9 and (i-1,j-1) not in already_flashed and (i-1,j-1) not in flash_pos:
                    flash_pos.append((i-1, j-1))

                inp[i-1][j+1] += 1
                if inp[i-1][j+1] > 9 and (i-1,j+1) not in already_flashed and (i-1,j+1) not in flash_pos:
                    flash_pos.append((i-1, j+1))

            if i == len(inp)-1:
                pass
            elif j == 0:
                inp[i+1][j] += 1
                if inp[i+1][j] > 9 and (i+1,j) not in already_flashed and (i+1,j) not in flash_pos:
                    flash_pos.append((i+1, j))

                inp[i+1][j+1] += 1
                if inp[i+1][j+1] > 9 and (i+1,j+1) not in already_flashed and (i+1,j+1) not in flash_pos:
                    flash_pos.append((i+1, j+1))
            elif j == len(inp[i])-1:
                inp[i+1][j] += 1
                if inp[i+1][j] > 9 and (i+1,j) not in already_flashed and (i+1,j) not in flash_pos:
                    flash_pos.append((i+1, j))

                inp[i+1][j-1] += 1
                if inp[i+1][j-1] > 9 and (i+1,j-1) not in already_flashed and (i+1,j-1) not in flash_pos:
                    flash_pos.append((i+1, j-1))
            else:
                inp[i+1][j] += 1
                if inp[i+1][j] > 9 and (i+1,j) not in already_flashed and (i+1,j) not in flash_pos:
                    flash_pos.append((i+1, j))

                inp[i+1][j-1] += 1
                if inp[i+1][j-1] > 9 and (i+1,j-1) not in already_flashed and (i+1,j-1) not in flash_pos:
                    flash_pos.append((i+1, j-1))

                inp[i+1][j+1] += 1
                if inp[i+1][j+1] > 9 and (i+1,j+1) not in already_flashed and (i+1,j+1) not in flash_pos:
                    flash_pos.append((i+1, j+1))
            
            if j == 0:
                inp[i][j+1] += 1
                if inp[i][j+1] > 9 and (i,j+1) not in already_flashed and (i,j+1) not in flash_pos:
                    flash_pos.append((i, j+1))
            elif j == len(inp[i])-1:
                inp[i][j-1] += 1
                if inp[i][j-1] > 9 and (i,j-1) not in already_flashed and (i,j-1) not in flash_pos:
                    flash_pos.append((i, j-1))
            else:
                inp[i][j-1] += 1
                if inp[i][j-1] > 9 and (i,j-1) not in already_flashed and (i,j-1) not in flash_pos:
                    flash_pos.append((i, j-1))

                inp[i][j+1] += 1
                if inp[i][j+1] > 9 and (i,j+1) not in already_flashed and (i,j+1) not in flash_pos:
                    flash_pos.append((i, j+1))
            
        for i, j in already_flashed:
            inp[i][j] = 0

    return flashes


def solve2(inp):
    k = 0
    while True:
        k += 1
        flash_pos = []

        for i, line in enumerate(inp):
            for j, num in enumerate(line):
                inp[i][j] += 1

                if num + 1 > 9:
                    flash_pos.append((i, j))
        
        already_flashed = []
        
        while flash_pos:
            i, j = flash_pos.pop(0)
            already_flashed.append((i,j))

            if i == 0:
                pass
            elif j == 0:
                inp[i-1][j] += 1
                if inp[i-1][j] > 9 and (i-1,j) not in already_flashed and (i-1,j) not in flash_pos:
                    flash_pos.append((i-1, j))

                inp[i-1][j+1] += 1
                if inp[i-1][j+1] > 9 and (i-1,j+1) not in already_flashed and (i-1,j+1) not in flash_pos:
                    flash_pos.append((i-1, j+1))
            elif j == len(inp[i])-1:
                inp[i-1][j] += 1
                if inp[i-1][j] > 9 and (i-1, j) not in already_flashed and (i-1, j) not in flash_pos:
                    flash_pos.append((i-1, j))

                inp[i-1][j-1] += 1
                if inp[i-1][j-1] > 9 and (i-1,j-1) not in already_flashed and (i-1,j-1) not in flash_pos:
                    flash_pos.append((i-1, j-1))
            else:
                inp[i-1][j] += 1
                if inp[i-1][j] > 9 and (i-1, j) not in already_flashed and (i-1, j) not in flash_pos:
                    flash_pos.append((i-1, j))

                inp[i-1][j-1] += 1
                if inp[i-1][j-1] > 9 and (i-1,j-1) not in already_flashed and (i-1,j-1) not in flash_pos:
                    flash_pos.append((i-1, j-1))

                inp[i-1][j+1] += 1
                if inp[i-1][j+1] > 9 and (i-1,j+1) not in already_flashed and (i-1,j+1) not in flash_pos:
                    flash_pos.append((i-1, j+1))

            if i == len(inp)-1:
                pass
            elif j == 0:
                inp[i+1][j] += 1
                if inp[i+1][j] > 9 and (i+1,j) not in already_flashed and (i+1,j) not in flash_pos:
                    flash_pos.append((i+1, j))

                inp[i+1][j+1] += 1
                if inp[i+1][j+1] > 9 and (i+1,j+1) not in already_flashed and (i+1,j+1) not in flash_pos:
                    flash_pos.append((i+1, j+1))
            elif j == len(inp[i])-1:
                inp[i+1][j] += 1
                if inp[i+1][j] > 9 and (i+1,j) not in already_flashed and (i+1,j) not in flash_pos:
                    flash_pos.append((i+1, j))

                inp[i+1][j-1] += 1
                if inp[i+1][j-1] > 9 and (i+1,j-1) not in already_flashed and (i+1,j-1) not in flash_pos:
                    flash_pos.append((i+1, j-1))
            else:
                inp[i+1][j] += 1
                if inp[i+1][j] > 9 and (i+1,j) not in already_flashed and (i+1,j) not in flash_pos:
                    flash_pos.append((i+1, j))

                inp[i+1][j-1] += 1
                if inp[i+1][j-1] > 9 and (i+1,j-1) not in already_flashed and (i+1,j-1) not in flash_pos:
                    flash_pos.append((i+1, j-1))

                inp[i+1][j+1] += 1
                if inp[i+1][j+1] > 9 and (i+1,j+1) not in already_flashed and (i+1,j+1) not in flash_pos:
                    flash_pos.append((i+1, j+1))
            
            if j == 0:
                inp[i][j+1] += 1
                if inp[i][j+1] > 9 and (i,j+1) not in already_flashed and (i,j+1) not in flash_pos:
                    flash_pos.append((i, j+1))
            elif j == len(inp[i])-1:
                inp[i][j-1] += 1
                if inp[i][j-1] > 9 and (i,j-1) not in already_flashed and (i,j-1) not in flash_pos:
                    flash_pos.append((i, j-1))
            else:
                inp[i][j-1] += 1
                if inp[i][j-1] > 9 and (i,j-1) not in already_flashed and (i,j-1) not in flash_pos:
                    flash_pos.append((i, j-1))

                inp[i][j+1] += 1
                if inp[i][j+1] > 9 and (i,j+1) not in already_flashed and (i,j+1) not in flash_pos:
                    flash_pos.append((i, j+1))
            
        for i, j in already_flashed:
            inp[i][j] = 0
        
        if len(already_flashed) == 100:
            break
    
    return k


path = "day11/day11_input.txt"
inp1 = read(path)
inp2 = read(path)

start = pfc()
print(f"The solution to part 1 is: {solve1(inp1)} in {pfc() - start} seconds")

start = pfc()
print(f"The solution to part 2 is: {solve2(inp2)} in {pfc() - start} seconds")
