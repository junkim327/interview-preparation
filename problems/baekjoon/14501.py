n = int(input())
t = [0] * n
p = [0] * n
for i in range(n):
    t[i], p[i] = map(int, input().split())
profit = 0

def get_max_profit(day, sum):
    global profit
    if day == n:
        profit = max(profit, sum)
        return
    if day > n:
        return
    get_max_profit(day+1, sum)
    get_max_profit(day+t[day], sum+p[day])

get_max_profit(0, 0)
print(profit)

