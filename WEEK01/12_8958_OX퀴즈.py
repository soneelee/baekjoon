# input에 입력되는 모든 것은 문자열로 취급한다

T = int(input())

for _ in range(T):
    a=input()
    
    temp = 0
    score = 0

    n = len(a)
    
    for i in range(n):
        if a[i] == 'O':
            temp += 1
            score = score + temp
        else:
            temp = 0

    print(score)

