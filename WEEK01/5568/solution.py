from itertools import permutations
#nPr

n = int(input())
r = int(input())
array = []
nums = []
num = ''

for _ in range(n):
    array.append(int(input()))

for i in permutations(array, r):
    # print(i, end=" ")
    for j in range(r):
        num += str(i[j])
    if num not in nums:
        nums.append(num)
    num = ''

print(len(nums))



 
