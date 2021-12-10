#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from time import perf_counter as pfc


def read(path: str):
    with open(path) as my_file:
        return [[bracket for bracket in line] for line in my_file.read().rstrip().split("\n")]


def solve1(inp):
    points_per_bracket = {')': 3, ']': 57, '}': 1197, '>': 25137}
    brackets = {'(': ')', '[': ']', '{': '}', '<': '>'}
    error_score = 0

    for line in inp:
        for i, char in enumerate(line):
            pass
    
    return error_score

def solve2(inp):
    pass


path = "day10/day10_sample.txt"
inp1 = read(path)
inp2 = read(path)

start = pfc()
print(f"The solution to part 1 is: {solve1(inp1)} in {pfc() - start} seconds")

start = pfc()
print(f"The solution to part 2 is: {solve2(inp2)} in {pfc() - start} seconds")
