# #### 방법 1 #####
# num = int(input())
# arry = []

# for _ in range(num):
#     arry.append(int(input()))

# #### 방법 2 #####
# arry = [None]*num

# for i in range(num):
#     arry[i] = int(input())


##### 버블 정렬 #####
# len = len(arry)

# cnt = 1

# while(cnt > 0):
#     cnt = 0
#     for i in range(len-1):#0~3
#         if (arry[i]>arry[i+1]):
#             arry[i],arry[i+1]=arry[i+1],arry[i]
#             cnt += 1

# print(arry)

# ##### 선택 정렬 #####
# arry = [5,4,3,2,1]

# len = len(arry)

# for i in range(len):
#     min = arry[i]
#     min_idx = i
#     for j in range(i+1, len):
#         if arry[j] < min:
#             min = arry[j]
#             min_idx = j
#     arry[i], arry[min_idx] = arry[min_idx], arry[i]


# print(arry)


# ##### 선택 정렬 solution #####
# def selectionSort(array):
#     for i in range(len(array)-1):
#         lowestNumberIndex = i
#         for j in range(i+1, len(array)):
#             if array[j] < array[lowestNumberIndex]:
#                 lowestNumberIndex = j

#         if lowestNumberIndex != i:
#             array[i], array[lowestNumberIndex] = array[lowestNumberIndex], array[i]

#     return array


# array = [5,4,3,2,1]
# selectionSort(array)
# print(array)


# ##### 삽입 정렬 #####
# array = [5,4,3,2,1]

# for i in range(1, len(array)):
#     temp = array[i]
#     array[i] = None
#     j=i-1
#     while j>=0:
#         if array[j] > temp:
#             array[j+1] = array[j]
#             array[j] = None
#             j -= 1
#     array[j+1] = temp

# print(array)

# ##### 삽입 정렬 solution #####

# def insertion_sort(array):
#     for index in range(1, len(array)):
#         temp_value = array[index]
#         #array[index] = None
#         position = index-1
#         while position >=0:
#             if array[position] > temp_value:
#                 array[position+1] = array[position]
#                 array[j] = None
#                 position -= 1
#             else:
#                 break
#         array[position+1] = temp_value
#     print(array)


# 버블정렬 개선 #############3
# 버블 정렬이라 부르는 이유 : 각 패스스루마다 정렬되지 않은 값 중 가장 큰 값, '버블'이 올바른 위치로 가게 된다.

# 버블 정렬 효율성 O(N^2)


def bubble_sort(list, flag=-1):
    unsorted_until_index = len(list) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(unsorted_until_index):
            if flag == i:
                continue
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
                sorted = False
            else:
                flag = i

        unsorted_until_index -= 1
        # 가장 큰 값은 정렬 되었다.

# 버블 정렬 효율성 O(N^2)
array = [5, 3, 1, 4, 2]
bubble_sort(array)
print(array)
