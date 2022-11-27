'''
    15989 - 1, 2, 3 더하기 4, https://www.acmicpc.net/problem/15989

    1 => 1
    2 => 1+1, 2
    3 => 1+1+1, 1+2, 3
    4 => 1+3, 1+1+2, 2+2, 1+1+1+1
    5 => 1+1+1+1+1, 1+1+1+2,| 1+1+3, 2+3,| 1+2+2
    6 => 1+1+1+3, 1+2+3, 3+3, 
    10 => 1+1+1+1+1+1
'''

import sys

read = sys.stdin.readline

def solve():
    T = int(read())
    dp = [0] * 100001
    dp[0] = 1
    dp[1], dp[2], dp[3], dp[4]= 1, 2, 3, 4
    last_max_n = 3
    for _ in range(T):
        n = int(read())
        if dp[n] != 0:
            print(dp[n])
            continue
        for i in range(last_max_n + 1, n + 1):
            dp[i] = dp[i - 3] + dp[i - 2] - dp[i - 5]  + 1
        last_max_n = n
        print(dp[n])

    return None


if __name__ == '__main__':
    solve()