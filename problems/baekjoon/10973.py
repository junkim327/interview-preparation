# 10973 - 이전 순열, https://www.acmicpc.net/problem/10973
def previous_premutation(a, n):
    i = n - 1
    while i > 0 and a[i-1] <= a[i]: i -= 1
    if i == 0: return False
    j = n - 1
    while a[i-1] <= a[j]: j -= 1
    a[i-1], a[j] = a[j], a[i-1]
    j = n - 1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
    return True

n = int(input())
a = list(map(int, input().split()))
if (previous_premutation(a, n)):
    print(' '.join(map(str, a)))
else:
    print(-1)