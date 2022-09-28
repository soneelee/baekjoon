import sys

num = int(sys.stdin.readline())
array = [0]*10001
for _ in range(num):
    array[int(sys.stdin.readline())] += 1

for i in range(10001):
    if array[i] != 0:
        for j in range(array[i]):
            print(i)

                 
           