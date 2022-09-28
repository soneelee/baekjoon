# 3 <= N <= 8
# 식 고정
# 배열 변경 - 순열 nPn(= n!)

import sys
from itertools import permutations

if __name__ == "__main__":
    N = int(input())
    array = list(map(int, sys.stdin.readline().split()))

    pmt = list(permutations(array))

    gap_array = []
    
    for i in range(len(pmt)):
        temp_array = list(pmt[i])
        gap = 0
        for j in range(N-1):
            gap += abs(temp_array[j] - temp_array[j+1])
            gap_array.append(gap)

    print(max(gap_array))


