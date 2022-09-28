import sys
# 한 줄 읽어 오기
n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
prime_nums = 0

# 1이 아닐 때,
# 2부터 해당 숫자의 바로 앞 숫자까지 for문 돌리기
# 나누어 떨어지면 temp > 0
# temp = 0 일 때 소수

for i in range(n):
    num = nums[i]
    if num != 1:
        temp = 0
        for j in range(2, num):
           if num % j == 0:
            temp += 1
        if temp == 0:
            prime_nums += 1
    
print(prime_nums)

#####함수 만드는 것이 깔끔한 듯#####
# def prime(x):
#     if x==1:
#         return 0
#     else:
#         for i in range(2,x-1):
#             if x%i==0:
#                 return 0
#         return 1
# T=int(input())
# A=list(map(int, input().split()))
# j=0
# for i in A:
#     j=j+prime(i)
# print(j)
# -----------------------------------------

# ##### 약수는 대칭임을 이용하여 절반만 확인 #####
# https://youtu.be/CyINCmJPjfM
# import math
# n=int(input())
# data=list(map(int,input().split()))
# cnt=0

# for i in data:
#     if i==1:continue
#     for j in range(2, int(math.sqrt(i))+1):
#         if i % j == 0:
#             break
#     else:
#         cnt += 1
# print(cnt)
# ___________________________________________
# print(9**2)
# 9^2 = 81

# print(9**0.5)
# 9^0.5 = 3

