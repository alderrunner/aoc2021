#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from time import perf_counter as pfc
import sys


def read(path: str):
    with open(path) as my_file:
        return [int(num) for num in my_file.read().rstrip().split(",")]


def solve1(inp):
    min_fuel = sys.maxsize 

    for i in range(len(inp)):
        fuel = 0

        for num in inp:
            fuel += abs(num-i)

        if fuel < min_fuel:
            min_fuel = fuel
    
    return min_fuel


def helper(num):
    res = 0

    for i in range(num+1):
        res += i
    
    return res


def solve2(inp):
    min_fuel = sys.maxsize

    for i in range(len(inp)):
        fuel = 0

        for num in inp:
            fuel += helper(abs(num-i))

        if fuel < min_fuel:
            min_fuel = fuel
    
    return min_fuel


path = "day07/day07_input.txt"
inp1 = read(path)
inp2 = read(path)

start = pfc()
print(f"The solution to part 1 is: {solve1(inp1)} in {pfc() - start} seconds")

start = pfc()
print(f"The solution to part 2 is: {solve2(inp2)} in {pfc() - start} seconds")
