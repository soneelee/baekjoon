# 문자열 != 리스트
# 테스트케이스는 입력 자료 수
T = int(input())

for _ in range(T):
    a = input()

    b = len(a)

    c = ""

    if b>2:
        for i in range(2,b):
            c += a[i] * int(a[0])

    print(c)