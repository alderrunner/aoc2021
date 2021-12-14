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
    # O(3*2^steps)
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
    template = inp[0]
    rules = inp[1]

    pair_occurrences = {pair: 0 for pair in rules.keys()}

    for i, element in enumerate(template):
        if i+1 >= len(template):
            break

        pair = element + template[i+1]
        pair_occurrences[pair] += 1
    
    all_elements = ''.join(set(rules.keys()))
    count = Counter(all_elements)

    for key in count.keys():
        count[key] = 0
        
    for elem in template:
        count[elem] += 1

    for _ in range(40):
        pair_occurrences_copy = pair_occurrences.copy()

        for i, pair in enumerate(pair_occurrences_copy.keys()):
            if pair_occurrences_copy[pair] == 0:
                continue

            rule = rules[pair]
            count[rule] += 1*pair_occurrences_copy[pair]

            pair_occurrences[pair] -= 1*pair_occurrences_copy[pair]
            pair_occurrences[pair[0]+rule] += 1*pair_occurrences_copy[pair]
            pair_occurrences[rule+pair[1]] += 1*pair_occurrences_copy[pair]
    
    return max(count.values()) - min(count.values())


path = "day14/day14_input.txt"
inp1 = read(path)
inp2 = read(path)

start = pfc()
print(f"The solution to part 1 is: {solve1(inp1)} in {pfc() - start} seconds")

start = pfc()
print(f"The solution to part 2 is: {solve2(inp2)} in {pfc() - start} seconds")
