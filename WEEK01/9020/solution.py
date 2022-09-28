# # 골드바흐의 추측은 2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있다는 것이다.
# # 짝수를 두 소수의 합으로 나타내는 표현을 그 수의 골드바흐 파티션이라 하고, 이 때의 두 소수는 골드바흐의 수 라고 한다.
# # 만약 가능한 n의 골드바흐 파티션이 여러 가지인 경우에는 두 소수의 차이가 가장 작은 것을 출력한다.
# # 에라토스테네스의 체 : 가장 대표적인 '소수 판별 알고리즘'
# # 소수를 대량으로 빠르고 정확하게 구하는 방법

import math

# 에라토스테네스의 체
n = 10000

a = [False, False] + [True]*(n-1)

for i in range(2, n+1):
    if a[i]:
        for j in range(2*i, n+1, i):
            a[j] = False

# 골드바흐의 수 구하기

# 테스트케이스 입력 받음
T = int(input())

for _ in range(T):  # 테스트케이스만큼 반복
    n = int(input())  # 짝수n = 소수1 + 소수2
    flag = False

    for i in range(math.ceil(n/2), n + 1):  # 정수 n/2 부터 n까지
        if a[i]:  # 소수1
            result = n - i  # 소수2
            for j in range(2, n//2+1):  # 2부터 n/2까지 소수2 탐색
                if result == j and a[j] == True:
                    print(j, i)  # 작은 소수부터 출력
                    flag = True  # 이중 for문 중단 flag
                    break
            # if result in a:
            #     print(a[i], result)
            #     break
                else:
                     continue

        if (flag):
            break
