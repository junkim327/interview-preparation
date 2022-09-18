# 7576 - 토마토, https://www.acmicpc.net/problem/7576

from collections import deque

def main():
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    m, n = map(int, input().split()) # m 가로칸 수, n 세로칸 수
    num_tomatoes = m * n
    tomatoes = []
    q = deque()
    days = 0

    for i in range(n):
        row = []
        for j, c in enumerate(input().split()):
            c = int(c)
            row.append(c)
            if c == -1:
                num_tomatoes -= 1
            elif c == 1:
                q.append((i, j))
                num_tomatoes -= 1
        tomatoes.append(row)

    while q:
        x, y = q.popleft()
        for i in range(4):
            x_i, y_i = x + dx[i], y + dy[i]
            if 0 <= x_i < n and 0 <= y_i < m:
                if tomatoes[x_i][y_i] == 0:
                    q.append((x_i, y_i))
                    tomatoes[x_i][y_i] = tomatoes[x][y] + 1
                    days = max(days, tomatoes[x][y] + 1)
                    num_tomatoes -= 1
                    
    
    if num_tomatoes != 0:
        print(-1)
    else:
        print(0 if days == 0 else days - 1)


if __name__ == '__main__':
    main()
