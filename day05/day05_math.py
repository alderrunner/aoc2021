from collections import defaultdict
from time import perf_counter as pfc


def read(path: str): # meins
    with open(path) as my_file:
        raw = my_file.read().rstrip()
        return [[[int(num) for num in points.split(",")] for points in line.split(" -> ")] for line in raw.splitlines()]


def sign(foo):
  if foo < 0:
    return -1
  elif foo == 0:
    return 0
  return 1

start = pfc()

points = defaultdict(int)
points_with_diags = defaultdict(int)

data = read("day05/day05_input.txt")

for line in data:
  sx = line[0][0]
  sy = line[0][1]
  ex = line[1][0]
  ey = line[1][1]
  l1 = abs(ex - sx)
  l2 = abs(ey - sy)
  s1 = sign(ex - sx)
  s2 = sign(ey - sy)
  for i in range(max(l1, l2)+1):
    x, y = sx+s1*i, sy+s2*i
    points_with_diags[x,y] += 1
    if min(l1, l2) == 0:
      points[x,y] += 1

print(len([c for c in points if points[c] > 1]))
print(len([c for c in points_with_diags if points_with_diags[c] > 1]), pfc() - start)