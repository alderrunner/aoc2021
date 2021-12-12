#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys
import numpy as np
from collections import Counter
from time import perf_counter as pfc


def read(path: str):
    with open(path) as my_file:
        raw = [line.split('-') for line in my_file.read().rstrip().splitlines()]
        adj = {}
        
        for line in raw:
            for element in line:
                adj[element] = []
        
        for line in raw:
            for i, element in enumerate(line):
                if i == 0:
                    adj[element].append(line[1])
                else:
                    adj[element].append(line[0])
        
        return adj


def dfs(start, end, inp, visited, path):
    if visited[start] == True:
        return
    
    if start.isupper():
        visited[start] = False
    else:
        visited[start] = True

    path.append(start)

    if start == end:
        paths.append(path.copy())
        visited[start] = False
        path.pop()
        return
    
    for next in inp[start]:
        dfs(next, end, inp, visited, path)

    path.pop()
    visited[start] = False


paths = []


def solve1(inp):
    visited = {vertex: False for vertex in inp.keys()}
    path = []

    dfs('start', 'end', inp, visited, path)
    
    return len(paths)


def solve2(inp):
    pass


path = "day12/day12_input.txt"
inp1 = read(path)
inp2 = read(path)

start = pfc()
print(f"The solution to part 1 is: {solve1(inp1)} in {pfc() - start} seconds")

start = pfc()
print(f"The solution to part 2 is: {solve2(inp2)} in {pfc() - start} seconds")
