# print('%.3f'%pct+'%') '%.3f'%숫자 소수점 뒤 세자리, 스트링이 된다.
# input()은 줄바꿈 당 하나씩 들어간다. 띄어쓰기 X
# 여기서는 숫자들을 리스트에 넣어야 하므로 list를 쓴다. map은 각각에 모두 적용시키기 위해 쓴다.

T = int(input())

for _ in range(T):
    sum = 0
    avg = 0
    temp = 0

    a = list(map(int,input().split()))
    num = a[0]
    for i in range(1,num+1):
        sum += a[i]
    avg = sum/num

    for i in range(1,num+1):
        if a[i] > avg:
            temp += 1

    pct = temp / num * 100

    print('%.3f'%pct+'%')