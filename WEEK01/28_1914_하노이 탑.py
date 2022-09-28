def hanoi(num, start, goal, other):
    global k
    if num == 1:
        print(start,goal)
        return

    #1 n-1 개 start-> other
    #2 1개 원판 start-> goal
    #3 n-1 개 other-> goal
    k += 1
    # hanoi(원판개수, 출발, 도착, 보조기둥)
    hanoi(num-1, start, other, goal)
    print(start,goal)
    hanoi(num-1, other, goal, start)
  

# 원판 개수 : n

# 1. 옮긴 횟수 k
# 2. 20이하 입력에 대해서 두번째 줄 부터 수행 과정 출력
# 3. 두 번째 줄부터 k개의 줄에 걸쳐 두 정수 a b를 빈칸을 사이에 두고

k = 0
num = int(input())

# hanoi(num, start, goal, other)
hanoi(num, 1, 3, 2)