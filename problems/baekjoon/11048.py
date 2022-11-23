# 11048 - 이동하기, https://www.acmicpc.net/problem/11048
# 점화식: dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + C[i][j]

import sys

def solve():
    read = sys.stdin.readline
    n, m = map(int, read().rstrip().split())
    p = list(map(int, read().rstrip().split()))
    for i in range(1, m):
        p[i] += p[i - 1]

    for i in range(n - 1):
        row = list(map(int, read().rstrip().split()))
        dp = [0] * m
        dp[0] = p[0] + row[0]
        for j in range(1, m):
            dp[j] = max(dp[j - 1], p[j]) + row[j]
        p = dp
    
    print(p[m - 1])

    return None

if __name__ == '__main__':
    solve()