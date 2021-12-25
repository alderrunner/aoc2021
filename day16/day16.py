#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from time import perf_counter as pfc
from functools import reduce


def read(path: str):
    with open(path) as my_file:
        hex_as_string = my_file.read().rstrip()
        binary = ''

        for char in hex_as_string:
            binary += format(int(char, 16), '04b')

        return binary


def match_literal(literal: str):
    information = ''
    literal_length = 1
    current_group = literal

    while current_group:
        match current_group[0]:
            case '1':
                information += current_group[1:5]
                literal_length += 1
                current_group = current_group[5:]
            case '0':
                information += current_group[1:5]
                break

    return literal_length*5, information


def parse(start: str, packet_num: int = 0):
    global versions
    versions += int(data[start:start+3], 2)
    curr_lit = []

    match data[start+3:start+6]:
        case '000':
            if data[start+6] == '0':
                end = start+22+int(data[start+7:start+22], 2)
                curr_start = start+22

                while curr_start < end:
                    curr_start, res = parse(curr_start)
                    curr_lit.append(res)

                return curr_start, sum(curr_lit)
            else:
                packet_num = int(data[start+7:start+18], 2)
                curr_start = start+18

                while packet_num > 0:
                    curr_start, res = parse(curr_start, packet_num)
                    curr_lit.append(res)
                    packet_num -= 1

                return curr_start, sum(curr_lit)
        case '001':
            if data[start+6] == '0':
                end = start+22+int(data[start+7:start+22], 2)
                curr_start = start+22

                while curr_start < end:
                    curr_start, res = parse(curr_start)
                    curr_lit.append(res)

                return curr_start, reduce((lambda x, y: x * y), curr_lit)
            else:
                packet_num = int(data[start+7:start+18], 2)
                curr_start = start+18

                while packet_num > 0:
                    curr_start, res = parse(curr_start, packet_num)
                    curr_lit.append(res)
                    packet_num -= 1

                return curr_start, reduce((lambda x, y: x * y), curr_lit)
        case '010':
            if data[start+6] == '0':
                end = start+22+int(data[start+7:start+22], 2)
                curr_start = start+22

                while curr_start < end:
                    curr_start, res = parse(curr_start)
                    curr_lit.append(res)

                return curr_start, min(curr_lit)
            else:
                packet_num = int(data[start+7:start+18], 2)
                curr_start = start+18

                while packet_num > 0:
                    curr_start, res = parse(curr_start, packet_num)
                    curr_lit.append(res)
                    packet_num -= 1

                return curr_start, min(curr_lit)
        case '011':
            if data[start+6] == '0':
                end = start+22+int(data[start+7:start+22], 2)
                curr_start = start+22

                while curr_start < end:
                    curr_start, res = parse(curr_start)
                    curr_lit.append(res)

                return curr_start, max(curr_lit)
            else:
                packet_num = int(data[start+7:start+18], 2)
                curr_start = start+18

                while packet_num > 0:
                    curr_start, res = parse(curr_start, packet_num)
                    curr_lit.append(res)
                    packet_num -= 1

                return curr_start, max(curr_lit)
        case '100':
            lit_len, literal = match_literal(data[start+6:])
            return start+6+lit_len, int(literal, 2)
        case '101':
            if data[start+6] == '0':
                end = start+22+int(data[start+7:start+22], 2)
                curr_start = start+22

                while curr_start < end:
                    curr_start, res = parse(curr_start)
                    curr_lit.append(res)

                return curr_start, 1 if curr_lit[0] > curr_lit[1] else 0
            else:
                packet_num = int(data[start+7:start+18], 2)
                curr_start = start+18

                while packet_num > 0:
                    curr_start, res = parse(curr_start, packet_num)
                    curr_lit.append(res)
                    packet_num -= 1

                return curr_start, 1 if curr_lit[0] > curr_lit[1] else 0
        case '110':
            if data[start+6] == '0':
                end = start+22+int(data[start+7:start+22], 2)
                curr_start = start+22

                while curr_start < end:
                    curr_start, res = parse(curr_start)
                    curr_lit.append(res)

                return curr_start, 1 if curr_lit[0] < curr_lit[1] else 0
            else:
                packet_num = int(data[start+7:start+18], 2)
                curr_start = start+18

                while packet_num > 0:
                    curr_start, res = parse(curr_start, packet_num)
                    curr_lit.append(res)
                    packet_num -= 1

                return curr_start, 1 if curr_lit[0] < curr_lit[1] else 0
        case '111':
            if data[start+6] == '0':
                end = start+22+int(data[start+7:start+22], 2)
                curr_start = start+22

                while curr_start < end:
                    curr_start, res = parse(curr_start)
                    curr_lit.append(res)

                return curr_start, 1 if curr_lit[0] == curr_lit[1] else 0
            else:
                packet_num = int(data[start+7:start+18], 2)
                curr_start = start+18

                while packet_num > 0:
                    curr_start, res = parse(curr_start, packet_num)
                    curr_lit.append(res)
                    packet_num -= 1

                return curr_start, 1 if curr_lit[0] == curr_lit[1] else 0


def solve1(inp: str):
    global versions
    global data
    versions = 0
    data = inp

    _, _ = parse(0)

    return versions


def solve2(inp):
    global versions
    global data
    versions = 0
    data = inp

    _, res = parse(0)

    return res


path = "day16/day16_input.txt"
inp1 = read(path)
inp2 = read(path)

start = pfc()
print(f"The solution to part 1 is: {solve1(inp1)} in {pfc() - start} seconds")

start = pfc()
print(f"The solution to part 2 is: {solve2(inp2)} in {pfc() - start} seconds")
