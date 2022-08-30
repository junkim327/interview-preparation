# 9095 - 1, 2, 3 더하기, https://www.acmicpc.net/problem/9095
def num_sum(sum, goal):
    if sum > goal: return 0
    if sum == goal: return 1
    cur_sum = 0
    for i in range(1, 4):
        cur_sum += num_sum(sum + i, goal)
    return cur_sum

def bottom_up(n):
    a[0] = 1
    for i in range(1, n + 1):
        if i - 1 >= 0:
            a[i] += a[i - 1]
        if i - 2 >= 0:
            a[i] += a[i - 2]
        if i - 3 >= 0:
            a[i] += a[i - 3]
    return a[n]

T = int(input())
for _ in range(T):
    n = int(input())
    #print(num_sum(0, n))

    a = [0] * (n + 1)
    print(bottom_up(n))

