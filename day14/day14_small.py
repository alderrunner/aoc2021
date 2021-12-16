from collections import Counter
from time import perf_counter as pfc

tpl, _, *rules = open('day14/day14_input.txt').read().split('\n')
rules = dict(r.split(" -> ") for r in rules)
start = pfc()
pairs = Counter(map(str.__add__, tpl, tpl[1:]))
chars = Counter(tpl)

for _ in range(40):
    for (a,b), c in pairs.copy().items():
        x = rules[a+b]
        pairs[a+b] -= c
        pairs[a+x] += c
        pairs[x+b] += c
        chars[x] += c

print(max(chars.values())-min(chars.values()), pfc()-start)