#!/usr/bin/env python3

def solve_part1():
    num_of_incr = 0

    with open('day01_input.txt', 'r') as my_file:
        last_depth = int(my_file.readline())

        for line in my_file:
            current_depth = int(line)

            if current_depth > last_depth:
                num_of_incr += 1
            
            last_depth = current_depth

    return num_of_incr


"""
def solve_part2():
    num_of_incr = 0

    with open('day01_sample.txt', 'r') as my_file:
        num1 = my_file.readline()
        num2 = my_file.readline()
        num3 = my_file.readline()

        current_sum = int(num1) + int(num2) + int(num3)
        print(current_sum)

        next_pos = len(num2) + len(num3) 
        my_file.seek(my_file.tell() - next_pos)
        print(my_file.tell())
        print(next(my_file))
"""


def solve_part2():
    num_of_incr = 0
    lines = None

    with open('day01_input.txt', 'r') as my_file:
        lines = my_file.readlines()

    if not lines:
        return

    last_sum = 0

    for i in range(len(lines)-2):
        num1 = int(lines[i].rstrip())
        num2 = int(lines[i+1].rstrip())
        num3 = int(lines[i+2].rstrip())

        current_sum = num1 + num2 + num3

        if current_sum > last_sum:
            num_of_incr += 1

        last_sum = current_sum
 
    return num_of_incr - 1


if __name__ == '__main__':
    print(f"The solution to part 1 is: {solve_part1()}")
    print(f"The solution to part 2 is: {solve_part2()}")

