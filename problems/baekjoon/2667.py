# 2667 - 단지번호붙이기, https://www.acmicpc.net/source/share/fdbc119d2337407fa8c0821470ec7606

from collections import deque

def main():

    def bfs(x, y):
        count = 1
        q = deque()
        q.append((x, y))
        a[x][y] = 0
        while q:
            x, y = q.popleft()
            for i in range(4):
                x_i, y_i = x + dx[i], y + dy[i]
                if 0 <= x_i < n and 0 <= y_i < n:
                    if a[x_i][y_i] == 1:
                        q.append((x_i, y_i))
                        a[x_i][y_i] = 0
                        count += 1
        
        return count

    def dfs(x, y, count):
        count += 1
        a[x][y] = 0
        for i in range(4):
            x_i, y_i = x + dx[i], y + dy[i]
            if 0 <= x_i < n and 0 <= y_i < n:
                if a[x_i][y_i] == 1:
                    count = dfs(x_i, y_i, count)
        
        return count


    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    n = int(input())
    a = [list(map(int, list(input()))) for _ in range(n)]
    num_houses_list = []

    for i in range(n):
        for j in range(n):
            if a[i][j] == 1:
                # num_houses_list.append(bfs(i, j))
                num_houses_list.append(dfs(i, j, 0))

    num_houses_list.sort()
    print(len(num_houses_list))
    print(*num_houses_list, sep='\n')


if __name__ == '__main__':
    main()