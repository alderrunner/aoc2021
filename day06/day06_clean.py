from collections import Counter
from time import perf_counter as pfc

if __name__ == '__main__':
    with open('day06/day06_input.txt') as f:
        ages = Counter([int(num) for num in f.read().split(',')])

    start = pfc()

    for _ in range(256):
        ages = {n: ages[n + 1] for n in range(-1, 8)}
        ages[8] = ages[-1]
        ages[6] += ages[-1]
        ages[-1] = 0

    print(sum(ages.values()), pfc()-start)