# 11052 - 카드 구매하기, https://www.acmicpc.net/problem/11052

num_cards = int(input()) # 카드의 개수
card_pack_prices = [0] + list(map(int, input().split())) # 카드팩 가격
memo = [0] * (num_cards + 1)

for i in range(1, num_cards + 1):
    for j in range(1, i + 1):
        memo[i] = max(memo[i], card_pack_prices[j] + memo[i - j])

print(memo[num_cards])