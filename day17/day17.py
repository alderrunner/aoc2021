#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from time import perf_counter as pfc
from itertools import product
from typing import List


def read(path: str):
    with open(path) as my_file:
        line = my_file.read().rstrip().split(':')[1].lstrip().split(',')
        tx_coords = [int(x) for x in line[0][2:].split('..')]
        ty_coords = [int(y) for y in line[1].lstrip()[2:].split('..')]

        txl = tx_coords[0]
        txr = tx_coords[1]
        tyb = ty_coords[0]
        tyt = ty_coords[1]
        
        return [txl, txr, tyb, tyt]


def reaches_target(velocity, target):
    curr_v = velocity
    curr_p = (0, 0)

    while curr_p[0] <= target[0][1] and curr_p[1] >= target[1][0]:
        if curr_p[0] >= target[0][0] and curr_p[0] <= target[0][1] and curr_p[1] >= target[1][0] and curr_p[1] <= target[1][1]:
            return True

        curr_p = (curr_p[0]+curr_v[0], curr_p[1]+curr_v[1])

        if curr_p[0] >= target[0][0] and curr_p[0] <= target[0][1] and curr_p[1] >= target[1][0] and curr_p[1] <= target[1][1]:
            return True
        
        if curr_v[0] > 0:
            curr_v = (curr_v[0]-1, curr_v[1]-1)
        else:
            curr_v = (0, curr_v[1]-1)

    return False


def calc_max(velocity):
    curr_v = velocity
    curr_p = (0, 0)
    max_y = 0

    while curr_v[1] >= 0:
        curr_p = (curr_p[0]+curr_v[0], curr_p[1]+curr_v[1])
        max_y = curr_p[1]

        if curr_v[0] > 0:
            curr_v = (curr_v[0]-1, curr_v[1]-1)
        else:
            curr_v = (0, curr_v[1]-1)
    
    return max_y


def solve1(inp):
    # (txl, txr), (tyb, tyt)
    target = [(inp[0], inp[1]), (inp[2], inp[3])]

    v_perms = list(product(range(inp[1]), range(inp[1]//2 + 2)))

    max_y = 0

    for velocity in v_perms:
        if reaches_target(velocity, target) and calc_max(velocity) > max_y:
            max_y = calc_max(velocity)

    return max_y


def solve2(inp):
    # (txl, txr), (tyb, tyt)
    target = [(inp[0], inp[1]), (inp[2], inp[3])]

    v_perms = list(product(range(inp[1]+1), range(-(inp[1]//2 + 2), inp[1]//2 + 2)))

    reachable = []

    for velocity in v_perms:
        if reaches_target(velocity, target):
            reachable.append(velocity)
    
    return len(reachable)


path = "day17/day17_input.txt"
inp1 = read(path)
inp2 = read(path)

start = pfc()
print(f"The solution to part 1 is: {solve1(inp1)} in {pfc() - start} seconds")

start = pfc()
print(f"The solution to part 2 is: {solve2(inp2)} in {pfc() - start} seconds")
