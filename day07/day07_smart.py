#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from time import perf_counter as pfc


def read(path: str):
    with open(path) as my_file:
        return [int(num) for num in my_file.read().rstrip().split(",")]


def median(a):
    a = sorted(a)

    n = len(a)
 
    # check for even case
    if n % 2 != 0:
        return int(a[n // 2])
     
    return int((a[int((n-1)/2)] + a[int(n / 2)])/2.0)


def solve1(inp):
    # Optimale Position ist der Median der Liste
    pos = median(inp)

    return sum([abs(x-pos) for x in inp])


def gsf(n):
    return n*(n+1)//2


def solve2(inp):
    fuel = []

    for pos in range(min(inp), max(inp)+1):
        f = sum([gsf(abs(x-pos)) for x in inp])
        fuel.append(f)
    
    return min(fuel)


path = "day07/day07_input.txt"
inp1 = read(path)
inp2 = read(path)

start = pfc()
print(f"The solution to part 1 is: {solve1(inp1)} in {pfc() - start} seconds")

start = pfc()
print(f"The solution to part 2 is: {solve2(inp2)} in {pfc() - start} seconds")
