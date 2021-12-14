#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from time import perf_counter as pfc
from collections import Counter


def read(path: str):
    with open(path) as my_file:
        both = my_file.read().rstrip().split('\n\n')
        template = [element for element in both[0].rstrip()]
        rules = {rule.split(' -> ')[0]: rule.split(' -> ')[1] for rule in both[1].splitlines()}
        
        return template, rules


def solve1(inp):
    template = inp[0]
    rules = inp[1]

    for _ in range(10):
        new_template = []

        for i, element in enumerate(template):
            if i+1 >= len(template):
                break

            pair = element + template[i+1]
            rule = rules[pair]

            if i == 0:
                new_template.append(element)
            new_template.append(rule)
            new_template.append(template[i+1])
        
        template = new_template
    
    count = Counter(template).values()

    return max(count) - min(count)


def solve2(inp):
    pass


path = "day14/day14_input.txt"
inp1 = read(path)
inp2 = read(path)

start = pfc()
print(f"The solution to part 1 is: {solve1(inp1)} in {pfc() - start} seconds")

start = pfc()
print(f"The solution to part 2 is: {solve2(inp2)} in {pfc() - start} seconds")
