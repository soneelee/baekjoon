# N개의 정수로 이루어진 배열 A가 주어진다. 이때, 배열에 들어있는 정수의 순서를 적절히 바꿔서 다음 식의 최댓값을 구하는 프로그램을 작성하시오.

# |A[0] - A[1]| + |A[1] - A[2]| + ... + |A[N-2] - A[N-1]|

# 첫째 줄에 N (3 ≤ N ≤ 8)이 주어진다. 둘째 줄에는 배열 A에 들어있는 정수가 주어진다. 배열에 들어있는 정수는 -100보다 크거나 같고, 100보다 작거나 같다.


from itertools import combinations
import sys
# 카드의 합이 21을 넘지 않는 한도 내에서, 카드의 합을 최대한 크게 만드는 게임

N = int(sys.stdin.readline())

# 띄어쓰기 받아오기
cards = list(map(int, sys.stdin.readline().split()))

card_combi = list(combinations(cards, 3))

sum_cards = []
gap = []

for i in range(len(card_combi)):
    if sum(card_combi[i]) <= M:
        sum_cards.append(sum(card_combi[i]))
        gap.append(abs(sum(card_combi[i]) - M))

# print(sum_cards)
# print(gap)
    
min_index = gap.index(min(gap))

print(sum_cards[min_index])
