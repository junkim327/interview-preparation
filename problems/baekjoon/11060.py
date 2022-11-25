# 11060 - 점프 점프, https://www.acmicpc.net/problem/11060
# 점화식: dp[i] = i번째 칸에 도착할 수 있는 최소 점프 횟수
# 고려한 사항: 1) 길이가 1이고 쓰여 있는 수가 0이면 return 0
#           2) 0이 두번 연속되면 두번째 0의 jump 배열을 확인해서 첫번째 0 이전 수로부터 jump가 가능했는지 확인

import sys

def solve():
    read = sys.stdin.readline
    n = int(read().rstrip())
    maze = list(map(int, read().rstrip().split()))
    jump = [0] * n

    for i in range(n - 1):
        if maze[i] == 0 and jump[i + 1] == 0:
            break
        for j in range(i + 1, i + maze[i] + 1):
            if j == n - 1:
                print(jump[i] + 1)
                return None
            if jump[j] == 0:
                jump[j] = jump[i] + 1
    
    print(0) if n == 1 else print(-1)
    return None

if __name__ == '__main__':
    solve()