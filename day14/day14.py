#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from time import perf_counter as pfc


def read(path: str):
    with open(path) as my_file:
        return my_file.read().rstrip()


def solve1(inp):
    pass


def solve2(inp):
    pass


path = "day14/day14_sample.txt"
inp1 = read(path)
inp2 = read(path)

start = pfc()
print(f"The solution to part 1 is: {solve1(inp1)} in {pfc() - start} seconds")

start = pfc()
print(f"The solution to part 2 is: {solve2(inp2)} in {pfc() - start} seconds")
