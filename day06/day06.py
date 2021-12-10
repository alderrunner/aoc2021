#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from time import perf_counter as pfc


def read(path):
    with open(path) as my_file:
        return [int(num) for num in my_file.read().rstrip().split(",")]


def solve1(data):
    for _ in range(80):
        for i in range(len(data)):
            if data[i] == 0:
                data[i] = 6
                data.append(8)
            else:
                data[i] -= 1
            
    return len(data)


def solve2(data):
    fish = {}
    for i in range(9):
        fish[i] = 0
    
    for num in data:
        fish[num] += 1

    for _ in range(256):
        new = fish[0]
        
        for i in range(8):
            fish[i] = fish[i+1]

        if new > 0:
            fish[8] = new
            fish[6] += new
        else:
            fish[8] = 0

    return sum(fish.values())


# Call by reference...
path = "day06/day06_input.txt"
inp1 = read(path)
inp2 = read(path)

start = pfc()
print(f"The solution to part 1 is: {solve1(inp1)} in {pfc() - start} seconds")

start = pfc()
print(f"The solution to part 2 is: {solve2(inp2)} in {pfc() - start} seconds")
