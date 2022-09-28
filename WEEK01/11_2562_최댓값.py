max = int(input())
num = 1
for i in range (8):
    a = int(input())
    if a > max:
        max = a
        num = i+2

print(max)
print(num)

############코드1############
# a = []

# for i in range(9) :
#     a.append(int(input()))

# aMax = max(a)

# print(aMax)
# print(a.index(aMax)+1)

############코드2############
#max_list=list(int(input()) for i in range(9))

