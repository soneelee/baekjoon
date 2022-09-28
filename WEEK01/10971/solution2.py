import sys
from itertools import permutations

N = int(sys.stdin.readline())

array2d = []

for _ in range(N):   
    array2d.append(list(map(int, sys.stdin.readline().split())))

cities = []

for i in range(N):
    cities.append(i)
print("cities", cities)

min_cost = 1e9
cost_list = []

for city in permutations(cities):
    total_cost = 0
    breaker = True
    print("city", city)
    for i in range(N-1):
        start = city[i]
        end = city[i+1]
        print(f"start : {start} -> end:{end}")
        cost = array2d[start][end]
        if cost == 0:
            breaker = False
            break
        total_cost += cost
    
    if breaker == False:
        continue
    
    #처음 출발지로 다시 회귀
    start = city[N-1]
    end = city[0]
    print(f"돌아감 / start : {start} -> end:{end}")
    cost = array2d[start][end]
    if cost == 0:
        break
    total_cost += cost

    if total_cost < min_cost:
        min_cost = total_cost

print(min_cost)

