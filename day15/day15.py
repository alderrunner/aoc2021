#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from time import perf_counter as pfc
from collections import defaultdict
from queue import PriorityQueue
import math


def read(path: str):
    with open(path) as my_file:
        lines =  my_file.read().rstrip().splitlines()

        adj = defaultdict(list)
        dist = defaultdict(int)

        for i, line in enumerate(lines):
            for j, num in enumerate(line):
                dist[(i, j)] = int(num)

                if i-1 >= 0:
                    adj[(i,j)].append((i-1,j))
                if i+1 < len(lines):
                    adj[(i,j)].append((i+1,j))
                if j-1 >= 0:
                    adj[(i,j)].append((i,j-1))
                if j+1 < len(line):
                    adj[(i,j)].append((i,j+1))
        
        return adj, dist


def extract_min(queue, D):
    min_d = math.inf
    min_vertex = None

    for vertex in queue:
        if D[vertex] < min_d:
            min_d = D[vertex]
            min_vertex = vertex
    
    return min_vertex


def solve1(inp):
    adj: dict = inp[0]
    dist = inp[1]

    path_dist = 0

    queue = PriorityQueue()
    prev: dict = {}
    D = defaultdict(int)
    visited = []

    for vertex in adj.keys():
        queue.put((math.inf, vertex))
        prev[vertex] = None
        D[vertex] = math.inf
    
    D[(0,0)] = 0
    queue.put((0, (0,0)))

    while not queue.empty():
        curr_v = queue.get()[1]
        visited.append(curr_v)

        if curr_v == (math.sqrt(len(adj))-1,math.sqrt(len(adj))-1):
            break

        for neighbor in set(adj[curr_v]).difference(visited):
            if D[curr_v] + dist[neighbor] < D[neighbor]:
                D[neighbor] = D[curr_v] + dist[neighbor]
                prev[neighbor] = curr_v
                queue.put((D[neighbor], neighbor))
    
    path = []
    u = (math.sqrt(len(adj))-1,math.sqrt(len(adj))-1)
    while u is not None:
        path.insert(0, u)
        u = prev[u]
    
    for vertex in path[1:]:
        path_dist += dist[vertex]
    
    return path_dist

def solve2(inp):
    pass


path = "day15/day15_input.txt"
inp1 = read(path)
inp2 = read(path)

start = pfc()
print(f"The solution to part 1 is: {solve1(inp1)} in {pfc() - start} seconds")

start = pfc()
print(f"The solution to part 2 is: {solve2(inp2)} in {pfc() - start} seconds")
