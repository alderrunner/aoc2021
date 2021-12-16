#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from time import perf_counter as pfc


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


def match_operator(operator: str):
    subpacket_total_length = 0

    match operator[0]:
        case '0':
            subpacket_total_length = int(operator[1:16], 2)
            current_subpacket_length = subpacket_total_length
            current_packet = operator[16:]

            while current_subpacket_length > 0:
                current_packet, current_subpacket_length = match_packet(current_packet, 0, current_subpacket_length)
            
            return operator[16+subpacket_total_length:]

        case '1':
            subpacket_number = int(operator[1:12], 2)
            current_packet = operator[12:]
            
            for _ in range(subpacket_number):
                current_packet = match_packet(current_packet, 1)
            
            return current_packet


def match_packet(packet: str, id: int=-1, subpacket_length: int=0):
    versions.append(int(packet[:3], 2))
    literal_length = -1

    match packet[3:6]:
        case '100':
            literal_length, _ = match_literal(packet[6:])
        case _:
            new_packet = match_operator(packet[6:])
    
    match id:
        case 0:
            if literal_length == -1:
                return new_packet, subpacket_length-(len(packet)-len(new_packet))
            subpacket_length -= 6+literal_length
            return packet[6+literal_length:6+literal_length+subpacket_length], subpacket_length
        case 1:
            if literal_length == -1:
                return new_packet
            return packet[6+literal_length:]
        case -1:
            pass


def solve1(inp):
    global versions
    versions = []

    match_packet(inp)

    return sum(versions)


def solve2(inp):
    pass


path = "day16/day16_input.txt"
inp1 = read(path)
inp2 = read(path)

start = pfc()
print(f"The solution to part 1 is: {solve1(inp1)} in {pfc() - start} seconds")

start = pfc()
print(f"The solution to part 2 is: {solve2(inp2)} in {pfc() - start} seconds")
