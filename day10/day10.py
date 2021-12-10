#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from io import open_code
from time import perf_counter as pfc


def read(path: str):
    with open(path) as my_file:
        return [[bracket for bracket in line] for line in my_file.read().rstrip().split("\n")]


def solve1(inp):
    points_per_bracket = {')': 3, ']': 57, '}': 1197, '>': 25137}
    brackets = {'(': ')', '[': ']', '{': '}', '<': '>'}
    ill_char = []

    for line in inp:
        open_br = []
        looking_for = []

        for i, char in enumerate(line):
            if i == 0 and char in brackets.items():
                break
            
            if char in brackets.keys():
                open_br.append(char)
                looking_for.append(brackets[char])
            else:
                if char == looking_for[-1]:
                    open_br.pop()
                    looking_for.pop()
                else:
                    ill_char.append(char)
                    break

    return sum([points_per_bracket[char] for char in ill_char])

def solve2(inp):
    brackets = {'(': ')', '[': ']', '{': '}', '<': '>'}
    ill_lines = []

    for i, line in enumerate(inp):
        open_br = []
        looking_for = []

        for j, char in enumerate(line):
            if j == 0 and char in brackets.items():
                break
            
            if char in brackets.keys():
                open_br.append(char)
                looking_for.append(brackets[char])
            else:
                if char == looking_for[-1]:
                    open_br.pop()
                    looking_for.pop()
                else:
                    ill_lines.append(i)
                    break
    
    ill_lines.sort(reverse=True)

    for i in ill_lines:
        inp.pop(i)
    
    pass


path = "day10/day10_input.txt"
inp1 = read(path)
inp2 = read(path)

start = pfc()
print(f"The solution to part 1 is: {solve1(inp1)} in {pfc() - start} seconds")

start = pfc()
print(f"The solution to part 2 is: {solve2(inp2)} in {pfc() - start} seconds")
