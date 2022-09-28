import sys
from itertools import combinations

dwarves = [None] * 9
sum_height = 0

for i in range(9):
    dwarves[i] = int(sys.stdin.readline())

dwarves_combi = list(combinations(dwarves, 7))
for j in range(len(dwarves_combi)):
    sum_height = sum(dwarves_combi[j])
    if sum_height == 100:
        dwarf = dwarves_combi[j]
        break    

dwarf= sorted(dwarf)

for x in dwarf[:7]:
  print(x)