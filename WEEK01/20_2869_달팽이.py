import sys
x = list(map(int, sys.stdin.readline().split()))
# x = [1, 2, 3, 4, 5]

a = x[0]
b = x[1]
v = x[2]

# 전체 길이에서 a 길이를 빼 준다.
# 하루가 지났을 때의 간격 = a-b로 나누었을 때,
# 나누어 떨어진다면 a길이 한 번만 더 가면 되니까, +1
# 나머지가 있다면, 나머지도 가고, a길이 한번 더 가야 하니까, +2

if (v-a) % (a-b) == 0:
    days = (v-a)//(a-b) + 1

else:
    days = (v-a)//(a-b) + 2

print(days)

#####올림 코드 사용#####
# res = 1 + (v - a) / (a - b)
# print(ceil(res))

#####반복문 돌리면 시간 초과#####
# days = 1
# dis = v-a

# while (dis>0):
#     days += 1
#     dis = dis + b - a

# print(days)
