'''
    11055 - 가장 큰 증가 부분 수열, https://www.acmicpc.net/problem/11055
'''

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    d = a[:]
    for i in range(n):
        for j in range(i):
            if a[j] < a[i] and d[i] < d[j] + a[i]:
                d[i] = d[j] + a[i]

    print(max(d))

    return None


if __name__ == '__main__':
    solve()