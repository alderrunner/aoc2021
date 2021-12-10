#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from time import perf_counter as pfc


def read(path: str):
    with open(path) as my_file:
        return [[part.strip().split() for part in line.split('|')] for line in my_file.read().rstrip().split('\n')]


def solve1(inp):
    counter = 0

    for line in inp:
        for i in range(4):
            if len(line[1][i]) == 2:
                counter += 1
            elif len(line[1][i]) == 3:
                counter += 1
            elif len(line[1][i]) == 4:
                counter += 1
            elif len(line[1][i]) == 7:
                counter += 1
    
    return counter


def solve2(inp):
    sum = 0

    for line in inp:
        top = mid = bottom = right_t = right_b = left_t = left_b = ''

        line[0].sort(key=len)

        eight = line[0].pop(9)
        four = line[0].pop(2)
        seven = line[0].pop(1)
        one = line[0].pop(0)

        top = set(seven).difference(one).pop()
        right_b = right_t = set(seven).intersection(one)

        mid = left_t = set(four).difference(one)

        bottom = left_b = set(eight).difference(mid.union(right_t).union(top))

        # Derive bottom and left_b from 9-4
        find_bot = set(four).union(top)
        for signal in line[0]:
            maybe = set(signal).difference(find_bot)
            is_inside = find_bot.intersection(signal) == find_bot

            if len(maybe) == 1 and is_inside:
                bottom = maybe.pop()
                left_b = left_b.difference(bottom).pop()

                break

        # Derive mid and left_t from 7-3 and bottom
        find_mid = set(seven).union(bottom)
        for signal in line[0]:
            maybe = set(signal).difference(find_mid)
            is_inside = find_mid.intersection(signal) == find_mid

            if len(maybe) == 1 and is_inside:
                mid = maybe.pop()
                left_t = left_t.difference(mid).pop()

                break
        
        # Derive right_b and right_t from 8-6 and what we know
        find_right = set(bottom).union(top).union(mid).union(left_b).union(left_t)
        for signal in line[0]:
            maybe = set(eight).difference(signal)
            is_inside = find_right.intersection(signal) == find_right

            if len(maybe) == 1 and is_inside:
                right_t = maybe.pop()
                right_b = right_b.difference(right_t).pop()

                break
    
        interpretation = {}

        s = list(eight)
        s.sort()
        eight = ''.join(s)

        s = list(seven)
        s.sort()
        seven = ''.join(s)

        s = list(four)
        s.sort()
        four = ''.join(s)

        s = list(one)
        s.sort()
        one = ''.join(s)

        interpretation[eight] = 8
        interpretation[seven] = 7
        interpretation[four] = 4
        interpretation[one] = 1

        for signal in line[0]:
            s = list(signal)
            s.sort()
            signal = ''.join(s)

            if set(signal) == set([top, bottom, left_t, left_b, right_t, right_b]):
                interpretation[signal] = 0
            elif set(signal) == set([top, mid, bottom, left_b, right_t]):
                interpretation[signal] = 2
            elif set(signal) == set([top, mid, bottom, right_t, right_b]):
                interpretation[signal] = 3
            elif set(signal) == set([top, mid, bottom, left_t, right_b]):
                interpretation[signal] = 5
            elif set(signal) == set([top, mid, bottom, left_t, left_b, right_b]):
                interpretation[signal] = 6
            else:
                interpretation[signal] = 9
        
        num = ''
        for signal in line[1]:
            s = list(signal)
            s.sort()
            signal = ''.join(s)

            if signal == 'bceg':
                print(signal)

            num += str(interpretation[signal])
        num = int(num)

        sum += num

    return sum


path = "day08/day08_input.txt"
inp1 = read(path)
inp2 = read(path)

start = pfc()
print(f"The solution to part 1 is: {solve1(inp1)} in {pfc() - start} seconds")

start = pfc()
print(f"The solution to part 2 is: {solve2(inp2)} in {pfc() - start} seconds")
