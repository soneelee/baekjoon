import sys
def fsort(a, max):
    '''도수 정렬(배열 원솟값은 0 이상 max 이하)'''
    n = len(a)           # 정렬할 배열 a
    f = [0] * (max + 1)  # 누적 도수 분포표 배열 f
    b = [0] * n          # 작업용 배열 b
    
    for i in range(n):    # 1. 도수 분포표 만들기
        f[a[i]] += 1
    
    for i in range(1, max + 1):    # 2. 누적 도수 분포표 만들기
        f[i] += f[i - 1]
        
    for i in range(n - 1, -1, -1):    # 3. 작업용 배열 만들기
        f[a[i]] -= 1
        b[f[a[i]]] = a[i]
        
    for i in range(n):    # 4. 배열 복사하기
        a[i] = b[i]

    

def counting_sort(a):
    fsort(a, max(a))



num = int(sys.stdin.readline())
array = [0]*10001
for _ in range(num):
    array[int(sys.stdin.readline())] += 1

# counting_sort(array)

for i in range(10001):
    if array[i] != 0:
            print(i)

                 
                # for j in range(array[i]):