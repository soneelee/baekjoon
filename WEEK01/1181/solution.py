# import sys

# # 1 ≤ N ≤ 20,000
# N = int(sys.stdin.readline())
# words = []

# for _ in range(N):
#     word = sys.stdin.readline()
#     if word not in words:





#         words.append(word)
#         print(word)
    

import sys

N = int(input())
words = []
for _ in range(N):
    words.append(sys.stdin.readline().rstrip())

words_set = list(set(words))
words_set.sort()
words_set.sort(key = lambda x : len(x))
for i in words_set:
    print(i)