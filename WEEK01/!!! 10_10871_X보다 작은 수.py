#map 함수의 반환 값은 map 객체라서 list나 tuple로 형 변환을 시켜주어야 함.
# map 함수란?
# : 리스트의 요소를 지정된 함수로 처리하는 함수. 

#   보통 여러 개의 데이터를 한 번에 다른 형태로 바꾸기 위해 사용함
n, x = map(int,input().split())

#여기선 int로 형변환 시켜주었기 때문에 문자열이 아니라서 list를 써 줌. 
# a = list(map(int,input().split()))
# 이렇게 하면 안 된다. a = int(input().split())
# 왜냐하면 int(스트링) 이어야 하는데 위 코드는 int(리스트) 이므로

a = input().split()
for i in range(n):
    if int(a[i]) < x:
        print(a[i], end=' ')


##########예제 입력##########
# 10 5
# 1 10 4 9 2 3 8 5 7 6

