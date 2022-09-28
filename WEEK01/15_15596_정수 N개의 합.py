# 함수만들기 문제!! 함수 복사해서 하기
# a: 합을 구해야 하는 정수 n개가 저장되어 있는 리스트 (0 ≤ a[i] ≤ 1,000,000, 1 ≤ n ≤ 3,000,000)
# 리턴값: a에 포함되어 있는 정수 n개의 합 (정수)

def solve(a):
    ans = 0
    n = len(a)

    for i in range(n):
        ans += a[i]
    return ans