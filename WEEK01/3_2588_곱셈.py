# 정수형 자료 입력 받기
a=int(input())
b=int(input())

print(a*(b%10))
print((a*((b%100)//10)))
print((a*(b//100)))
print(a*b)

#input()은 값을 string으로 받는다 따라서 123은 백이십삼이 아니라 1,2,3 이다
# a = int(input())
# b = input()

# a1 = a * int(b[2])
# a2 = a * int(b[1])
# a3 = a * int(b[0])
# a4 = a * int(b)

# print (a1, a2, a3, a4, sep='\n')
# 줄바꿈으로 구분한다
