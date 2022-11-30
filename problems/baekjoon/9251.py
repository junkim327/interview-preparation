# 9251 - LCS, https://www.acmicpc.net/problem/9251

import sys

read = sys.stdin.readline

def solve():
    str1 = read().rstrip()
    str2 = read().rstrip()
    str1_len = len(str1)
    str2_len = len(str2)
    dp = [[0] * (str2_len + 1) for _ in range(str1_len + 1)]

    for i in range(str1_len - 1, -1, -1):
        for j in range(str2_len - 1, -1, -1):
            if str1[i] == str2[j]:
                dp[i][j] = dp[i + 1][j + 1] + 1
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

    print(dp[0][0])
    
    return None

if __name__ == '__main__':
    solve()
