# 7562 - 나이트의 이동, https://www.acmicpc.net/problem/7562

from collections import deque

def main():

    def bfs(x, y):
        q = deque()
        q.append((x, y))
        chess_board[x][y] = 0
        while q:
            x, y = q.popleft()
            for i in range(8):
                x_i, y_i = x + dx[i], y + dy[i]
                if 0 <= x_i < l and 0 <= y_i < l:
                    if chess_board[x_i][y_i] == -1:
                        q.append((x_i, y_i))
                        chess_board[x_i][y_i] = chess_board[x][y] + 1


    dx = [1, 2, 2, 1, -1, -2, -2, -1]
    dy = [2, 1, -1, -2, -2, -1, 1, 2]

    n = int(input())
    for _ in range(n):
        l = int(input())
        x_start, y_start = map(int, input().split())
        x_end, y_end = map(int, input().split())
        chess_board = [[-1] * l for _ in range(l)]
        bfs(x_start, y_start)
        print(chess_board[x_end][y_end])


if __name__ == '__main__':
    main()