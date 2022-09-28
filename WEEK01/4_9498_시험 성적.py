# if문 로직 : 만족하면 바로 빠져 나온다
# 입력 조건을 잘 본다. '정수', '값의 범위'
score=int(input())

if 90 <= score <= 100:
    print('A')

elif 80 <= score:
    print('B')

elif 70 <= score:
    print('C')

elif 60 <= score:
    print('D')

else: print('F')
       