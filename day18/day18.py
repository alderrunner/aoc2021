#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from time import perf_counter as pfc


def read(path: str):
    with open(path) as my_file:
        # Binary Trees!
        return my_file.read().rstrip()


def explode(sf_num, pos):
    exploding = sf_num[pos[0]][pos[1]][pos[2]][pos[3]]
    sf_num[pos[0]][pos[1]][pos[2]][pos[3]] = 0

    match pos[3]:
        case '0':
            sf_num[pos[0]][pos[1]][pos[2]][1] += exploding[1]
        case '1':
            sf_num[pos[0]][pos[1]][pos[2]][1] += exploding[0]


def split():
    pass


def solve1(inp):
    pass


def solve2(inp):
    pass


path = "day18/day18_sample.txt"
inp1 = read(path)
inp2 = read(path)

start = pfc()
print(f"The solution to part 1 is: {solve1(inp1)} in {pfc() - start} seconds")

start = pfc()
print(f"The solution to part 2 is: {solve2(inp2)} in {pfc() - start} seconds")
