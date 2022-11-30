# 9252 - LCS 2, https://www.acmicpc.net/problem/9252

import sys

read = sys.stdin.readline

def solve():
    str1 = read().rstrip()
    str2 = read().rstrip()
    str1_len = len(str1)
    str2_len = len(str2)
    dp = [[0] * (str2_len + 1) for _ in range(str1_len + 1)]
    p = [[0] * (str2_len + 1) for _ in range(str1_len + 1)]

    for i in range(str1_len - 1, -1, -1):
        for j in range(str2_len - 1, -1, -1):
            if str1[i] == str2[j]:
                dp[i][j] = dp[i + 1][j + 1] + 1
                p[i][j] = 1
            else:
                if dp[i + 1][j] >= dp[i][j + 1]:
                    dp[i][j] = dp[i + 1][j]
                    p[i][j] = 2
                else:
                    dp[i][j] = dp[i][j + 1]
                    p[i][j] = 3

    print(dp[0][0])

    i, j = 0, 0
    while p[i][j] != 0:
        if str1[i] == str2[j]:
            print(str1[i], end='')
        if p[i][j] == 1:
            i += 1
            j += 1
        elif p[i][j] == 2:
            i += 1
        elif p[i][j] == 3:
            j += 1
    
    print()
    
    return None

if __name__ == '__main__':
    solve()
