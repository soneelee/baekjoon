# str 스트링 변환을 적절히 사용하자
# 문자열은 문자열끼리, 숫자는 숫자끼리 비교해야 한다.
# count 하는 함수도 있다.
# for i in range(10)
#     d.count(str(i))
#     print(i)

a = int(input())
b = int(input())
c = int(input())

d = str(a*b*c)

for i in range(10):
    temp = 0    
    for j in range(len(d)):
        if d[j] == str(i):
            temp += 1
    print(temp)    