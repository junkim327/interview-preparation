# 2178 - 미로 탐색, https://www.acmicpc.net/problem/2178
# 문제가 최단 경로를 찾을때는 bfs를 사용.

from collections import deque

def main():

    def bfs(x, y):
        q = deque()
        q.append((x, y))
        check[x][y] = True
        while q:
            x, y = q.popleft()
            for i in range(4):
                x_i, y_i = x + dx[i], y + dy[i]
                if 0 <= x_i < n and 0 <= y_i < m:
                    if a[x_i][y_i] == 1 and not check[x_i][y_i]:
                        q.append((x_i, y_i))
                        a[x_i][y_i] = a[x][y] + 1
                        check[x_i][y_i] = True

                        
                        
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    n, m = map(int, input().split())
    a = [list(map(int, list(input()))) for _ in range(n)]
    check = [[False] * m for _ in range(n)]

    bfs(0, 0)
    print(a[n - 1][m - 1])


if __name__ == '__main__':
    main()