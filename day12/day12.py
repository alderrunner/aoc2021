#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from collections import defaultdict
from time import perf_counter as pfc


def read(path: str):
    with open(path) as my_file:
        lines = my_file.read().rstrip().splitlines()
        adj = defaultdict(list)
        
        for line in lines:
            a, b = line.split('-')
            adj[a].append(b)
            adj[b].append(a)
        
        return adj


def solve1(inp):
    def dfs(cur, seen):
        if cur == 'end':
            return 1
        
        if cur.islower() and cur in seen:
            return 0

        seen = seen | {cur}
        out = 0

        for thing in inp[cur]:
            out += dfs(thing, seen)

        return out
    
    return dfs('start', set())


def solve2(inp):
    pass


path = "day12/day12_sample.txt"
inp1 = read(path)
inp2 = read(path)

start = pfc()
print(f"The solution to part 1 is: {solve1(inp1)} in {pfc() - start} seconds")

start = pfc()
print(f"The solution to part 2 is: {solve2(inp2)} in {pfc() - start} seconds")
