from itertools import combinations
import sys
# 카드의 합이 21을 넘지 않는 한도 내에서, 카드의 합을 최대한 크게 만드는 게임

N, M = map(int, sys.stdin.readline().split())

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
