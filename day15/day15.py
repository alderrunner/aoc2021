#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from time import perf_counter as pfc
from collections import defaultdict
import heapq
import math


def read(path: str):
    with open(path) as my_file:
        lines =  my_file.read().rstrip().splitlines()

        adj = defaultdict(list)
        weights = defaultdict(int)

        for i, line in enumerate(lines):
            for j, num in enumerate(line):
                weights[(i, j)] = int(num)

                if i-1 >= 0:
                    adj[(i,j)].append((i-1,j))
                if i+1 < len(lines):
                    adj[(i,j)].append((i+1,j))
                if j-1 >= 0:
                    adj[(i,j)].append((i,j-1))
                if j+1 < len(line):
                    adj[(i,j)].append((i,j+1))
        
        return adj, weights


def lazy_dijkstra(adj: dict, weights: dict):
    dist = {}
    visited = {}
    prev = {}

    for point in adj.keys():
        dist[point] = float('inf')
        visited[point] = False
        prev[point] = None

    dist[(0,0)] = 0
    pq = [(0, (0,0))]

    while len(pq) > 0:
        _, curr_v = heapq.heappop(pq)

        if curr_v == (int(math.sqrt(len(adj)))-1,int(math.sqrt(len(adj)))-1): break

        if visited[curr_v]: continue

        visited[curr_v] = True

        for neighbor in adj[curr_v]:
            if dist[curr_v] + weights[neighbor] < dist[neighbor]:
                dist[neighbor] = dist[curr_v] + weights[neighbor]
                prev[neighbor] = curr_v
                heapq.heappush(pq, (dist[neighbor],neighbor))

    return dist, prev


def solve1(inp):
    adj: dict = inp[0]
    dist = inp[1]

    dist, _ = lazy_dijkstra(adj, dist)
    
    return dist[int(math.sqrt(len(adj)))-1,int(math.sqrt(len(adj)))-1]


def solve2(inp):
    pass


path = "day15/day15_input.txt"
inp1 = read(path)
inp2 = read(path)

start = pfc()
print(f"The solution to part 1 is: {solve1(inp1)} in {pfc() - start} seconds")

start = pfc()
print(f"The solution to part 2 is: {solve2(inp2)} in {pfc() - start} seconds")
