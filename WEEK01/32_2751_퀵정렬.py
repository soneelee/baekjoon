# num = int(input())
# arr = []
# for _ in range(num):
#     arr.append(int(input()))

# def quick_sort (arr, start, end):
#     # 원소가 1개인 경우 함수 종료
#     if start >= end: 
#         return
#     # 첫 번째 원소를 피벗으로 설정
#     pv = start
#     # 좌측 리스트 시작점
#     left = start + 1
#     # 우측 리스트 시작점
#     right = end
    
#     while left <= right:
    
#       # 피벗보다 큰 값을 찾을 때까지 무한 반복문
#         while left <= end and arr[left] <= arr[pv]:
#             left += 1 

#       # 피벗보다 작은 값을 찾을 때까지 문한 반복문
#         while right > start and arr[right] >= arr[pv]:
#             right -= 1

#       # 탐색하는 데이터 위치가 다른 경우(엇갈린 경우)
#         if left > right:
#             arr[right], arr[pv] = arr[pv], arr[right]
#         else:
#             arr[left], arr[right] = arr[right], arr[left]
#     # 분할 이후 좌측 및 우측 리스트 각각에에 대해 퀵 정렬 수행
#     quick_sort(arr, 0, right -1)
#     quick_sort(arr, right + 1, end) 

# quick_sort(arr, 0, len(arr)-1)
# print(arr)



# list.sort(arr)

# for i in range(num):
#     print(arr[i])



import sys

num = int(sys.stdin.readline())
array = []
for _ in range(num):
    array.append(int(sys.stdin.readline()))

list.sort(array)

for a in array:
    print(a)