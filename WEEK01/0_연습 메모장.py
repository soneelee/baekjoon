# a = 3
# print('%.3f'%a+'바보')

# -------------------------------

# import math

# number = int(input())
# a = []

# def primeNumberSeive():
#     for i in range(2, number+1):
#         a[i] = i

#     for i in range(2, number+1):
#         if a[i] == 0:
#             continue
        
#         else:
#             #  다 할 필요 없이, 배수들만 확인 해주면 되니까  
#             for j in range(i+i, number+1, i):
#                 if a[j] % a[i] == 0:
#                     a[j] = 0

# temp = math.ceil(number/10)
# for i in range(1, temp+1):
#     for j in range(10*(i-1)+1,10*i + 1):
#         print(a[j], end=" ")
#         print("\n")




# arr = [[0 for j in range(cols)] for i in range(rows)]

# n = 1000 # 2부터 1,000까지의 모든 수에 대하여 소수 판별
# array = [True for i in range(n + 1)] # 처음엔 모든 수가 소수(True)인 것으로 초기화



