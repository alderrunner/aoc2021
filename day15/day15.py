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


def weird_mod(num: int):
    if num+1 > 9:
        return 1
    return num+1


def extend_line(line: str):
    added_line = line
    curr_line = line

    for _ in range(4):
        next_line = ''

        for char in curr_line:
            next_line += str(weird_mod(int(char)))
        
        curr_line = next_line
        added_line += next_line
    
    return added_line


def add_line(line: str):
    added_line = ''

    for char in line:
        added_line += str(weird_mod(int(char)))
    
    return added_line


def read2(path: str):
    with open(path) as my_file:
        lines =  my_file.read().rstrip().splitlines()

        adj = defaultdict(list)
        weights = defaultdict(int)
        data = []

        for line in lines:
            data.append(extend_line(line))
        
        original_length = len(lines)
        
        for i in range(4):
            start = i*original_length
            end = ((i+1)*original_length)

            for j in range(start, end):
                data.append(add_line(data[j]))
        
        for i, line in enumerate(data):
            for j, num in enumerate(line):
                weights[(i, j)] = int(num)

                if i-1 >= 0:
                    adj[(i,j)].append((i-1,j))
                if i+1 < len(data):
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
    weights = inp[1]

    dist, _ = lazy_dijkstra(adj, weights)
    
    return dist[int(math.sqrt(len(adj)))-1,int(math.sqrt(len(adj)))-1]


def solve2(inp):
    adj_2: dict = inp[0]
    weights = inp[1]

    dist, _ = lazy_dijkstra(adj_2, weights)
    
    return dist[int(math.sqrt(len(adj_2)))-1,int(math.sqrt(len(adj_2)))-1]


path = "day15/day15_input.txt"
inp1 = read(path)
inp2 = read2(path)

start = pfc()
print(f"The solution to part 1 is: {solve1(inp1)} in {pfc() - start} seconds")

start = pfc()
print(f"The solution to part 2 is: {solve2(inp2)} in {pfc() - start} seconds")
