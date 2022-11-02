'''
    2156 - 포도주 시식, https://www.acmicpc.net/problem/2156
    
    점화식: d[n]: n개의 포도주 잔까지 최대로 마실 수 있는 포도주의 양
           d[n] = max(d[n-1], d[n-2] + a[n], d[n-3] + a[n-1] + a[n])
'''

def solve():
    n = int(input())
    a = [0] * (n + 1)
    for i in range(1, n + 1):
        a[i] = int(input())
    
    if n == 1:
        print(a[1])
        return None
    elif n == 2:
        print(a[1] + a[2])
        return None
    else:
        d = [0] * (n + 1)
        d[1] = a[1]
        d[2] = a[1] + a[2]
        for i in range(2, n + 1):
            d[i] = max(d[i - 1], d[i - 2] + a[i], d[i - 3] + a[i - 1] + a[i])
        print(d[n])
        return None

    return None


def solve2():
    a = [int(input()) for i in range(int(input()))]
    d = [0, a[0], 0]
    for i in a[1:]:
        d = [max(d), d[0] + i, d[1] + i]
    print(max(d))


if __name__ == '__main__':
    #solve()
    solve2()