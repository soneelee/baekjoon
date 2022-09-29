import sys
from itertools import permutations

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

cards = []
selectCards = []
nums = []


for _ in range(n):
    cards.append(sys.stdin.readline().strip())
    # 정수 아님. 공백 제거

for temp in permutations(cards, k):
    # print(temp, end =" ")
    num = ''
    for i in range(k):
        num += temp[i]
    if num not in nums:
        nums.append(num)

print(len(nums))