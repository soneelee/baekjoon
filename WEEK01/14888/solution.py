# N개의 수로 이루어진 수열 A1, A2, ..., AN
# 수와 수 사이에 끼워넣을 수 있는 N-1개의 연산자
# 덧셈, 뺄셈, 곱셈, 나눗셈
# 최댓값
# 최솟값

import sys
from itertools import permutations

N = int(sys.stdin.readline())

nums = list(map(str, sys.stdin.readline().split()))
operators = list(map(int, sys.stdin.readline().split()))

# print(sum(operators))
oper_list=[]

for i in range(4): 
    for _ in range(operators[i]):
        if i == 0:
            oper_list.append('+')
        elif i == 1:
            oper_list.append('-')
        elif i == 2:
            oper_list.append('*')
        else:
            oper_list.append('//')

oper_set = list(set(permutations(oper_list)))
equations = []

result = []
answer = 0
n = 0
for i in range(len(oper_set)):
    equation = nums[0]
    for j in range(N-1):
        if oper_set[i][j] == '//' and int(equation) < 0:
            equation = str(-int(equation))
            equation += oper_set[i][j]
            equation += nums[j+1]
            equation = str(-eval(equation))
            continue
        equation += oper_set[i][j]
        equation += nums[j+1]
        equation = str(eval(equation))
        # print(f"temp{j+1} : {equation}")  

    result.append(eval(equation))
    n += 1
    # print(f"equation{n} : {equation}")
   
print(max(result))    
print(min(result))




# print(oper_set)

# permutations()

