# 논리 연산자 우선 순위
year=int(input())

if (year%4==0 and year%100!=0) or (year%400)==0:
        print('1')
else:
        print('0')
