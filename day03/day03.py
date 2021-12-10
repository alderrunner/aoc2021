#!/usr/bin/env python3

from time import perf_counter as pfc


def read_input(path: str):
    with open(path) as my_file:
        return [line.rstrip() for line in my_file.readlines()]


def solve_part1():
    data = read_input('day03_input.txt')
    gamma_rate = ''
    epsilon_rate = ''
    
    for i in range(len(data[0])):
        count_of_ones = sum([int(data[j][i]) for j in range(len(data))])

        if count_of_ones > len(data) - count_of_ones:
            gamma_rate += '1'
            epsilon_rate += '0'
        else:
            gamma_rate += '0'
            epsilon_rate += '1'

    return int(gamma_rate, 2) * int(epsilon_rate, 2)


def solve_part2():
    data = read_input('day03_input.txt')

    for i in range(len(data[0])):
        indexes_ones = []
        indexes_zeros = []
        count_of_ones = 0
        count_of_zeros = 0
        
        for j in range(len(data)):
            if data[j][i] == '1':
                indexes_ones.append(j)
                count_of_ones += 1
            else:
                indexes_zeros.append(j)
                count_of_zeros += 1

        if count_of_ones >= count_of_zeros:
            for j in sorted(indexes_zeros, reverse = True):
                data.pop(j)
        else:
            for j in sorted(indexes_ones, reverse = True):
                data.pop(j) 

        if len(data) == 1:
            break

    oxygen_rating = int(data[0], 2)

    data = read_input('day03_input.txt')

    for i in range(len(data[0])):
        indexes_ones = []
        indexes_zeros = []
        count_of_ones = 0
        count_of_zeros = 0
        
        for j in range(len(data)):
            if data[j][i] == '1':
                indexes_ones.append(j)
                count_of_ones += 1
            else:
                indexes_zeros.append(j)
                count_of_zeros += 1

        if count_of_ones >= count_of_zeros:
            for j in sorted(indexes_ones, reverse = True):
                data.pop(j)
        else:
            for j in sorted(indexes_zeros, reverse = True):
                data.pop(j)
        
        if len(data) == 1:
            break

    co2_rating = int(data[0], 2)

    return co2_rating * oxygen_rating


if __name__ == '__main__':
    start = pfc()
    print(f"The solution to part 1 is: {solve_part1()} in {pfc()-start}")
    start = pfc()
    print(f"The solution to part 2 is: {solve_part2()} in {pfc()-start}")
