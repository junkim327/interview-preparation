# 5582 - 공통 부분 문자열, https://www.acmicpc.net/problem/5582

import sys

read = sys.stdin.readline

def solve():
    s1, s2 = ' ' + read().rstrip(), ' ' + read().rstrip()
    s1_len, s2_len = len(s1), len(s2)
    dp = [[0] * s2_len for _ in range(s1_len)]
    
    max_len = 0
    for i in range(1, s1_len):
        for j in range(1, s2_len):
            if s1[i] == s2[j]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                max_len = max(max_len, dp[i - 1][j - 1] + 1)
            else:
                dp[i][j] = 0

    print(max_len)

    return None


if __name__ == '__main__':
    solve()