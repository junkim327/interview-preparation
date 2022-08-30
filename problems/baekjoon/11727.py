# 11727 - 2xn 타일링 2, https://www.acmicpc.net/problem/11727
# 시간 제한 1초, input: 1 <= n <= 1000

def bottom_up(n):
    if n == 1:
        return 1
    if n == 2:
        return 3
    a[1], a[2] = 1, 3
    for i in range(3, n+1):
        a[i] = a[i-1] + a[i-2] * 2
    return a[n] % 10007

n = int(input())
a = [0] * (n+1)
print(bottom_up(n))