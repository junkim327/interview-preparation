# 11726 - 2xn 타일링, https://www.acmicpc.net/problem/11726

def bottom_up(n):
    a[1], a[2] = 1, 2
    for i in range(3, n+1):
        a[i] = a[i-1] + a[i-2]

    return a[n] % 10007

n = int(input())
a = [0] * (n+1)
if n <= 3:
    print(n)
else:
    print(bottom_up(n))
