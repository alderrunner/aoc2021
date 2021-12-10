#!/usr/bin/env python3

from time import perf_counter as pfc


def read_input():
    with open('day02_input.txt') as my_file:
        return [line.rstrip().split(' ') for line in my_file.readlines()]


def solve_part1():
    data = read_input()
    pos = 0
    depth = 0

    for row in data:
        operation = row[0]
        units = int(row[1])
        
        if operation == 'forward':
            pos += units
        elif operation == 'down':
            depth += units
        else:
            depth -= units

    return pos, depth, pos * depth


def solve_part2():
    data = read_input()
    pos = 0
    depth = 0
    aim = 0

    for row in data:
        operation = row[0]
        units = int(row[1])

        if operation == 'down':
            aim += units
        elif operation == 'up':
            aim -= units
        else:
            pos += units
            depth += aim * units

    return pos, depth, aim, pos * depth


if __name__ == '__main__':
    start = pfc()
    print(f"The solution to part 1 is: {solve_part1()[2]} in {pfc()-start}")

    start = pfc()
    print(f"The solution to part 2 is: {solve_part2()[3]} in {pfc()-start}")

