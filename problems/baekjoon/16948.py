# 16948 - 데스 나이트, https://www.acmicpc.net/problem/16948
# 문제 힌트: '최소 이동 횟수를 구해보자' -> BFS

from collections import deque

def solve():
    dir = [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]
    n = int(input())
    r1, c1, r2, c2 = map(int, input().split())

    dist = list([-1] * n for _ in range(n))
    dist[r1][c1] = 0
    q = deque()
    q.append((r1, c1))
    while q:
        r, c = q.popleft()
        for i, j in dir:
            dr, dc = r + i, c + j
            if dr == r2 and dc == c2:
                print(dist[r][c] + 1)
                return

            if 0 <= dr < n and 0 <= dc < n and dist[dr][dc] == -1:
                q.append((dr, dc))
                dist[dr][dc] = dist[r][c] + 1
    
    print(-1)

    return None


if __name__ == '__main__':
    solve()