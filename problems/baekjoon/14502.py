# 14502 - 연구소, https://www.acmicpc.net/problem/14502

from itertools import combinations
from collections import deque

def solve():
    dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    n, m = map(int, input().split())
    grid = []
    empty_spaces =[]
    q = deque()

    for i in range(n):
        row = list(map(int, input().split()))
        for j in range(m):
            if row[j] == 0:
                empty_spaces.append((i, j))
            elif row[j] == 2:
                q.append((i, j))
        grid.append(row)
    
    num_empty_spaces = len(empty_spaces)
    max_num_safe_blocks = -1
    for subsequences in combinations(range(num_empty_spaces), 3):
        copied_grid = [b[:] for b in grid]
        for seq in subsequences:
            x, y = empty_spaces[seq]
            copied_grid[x][y] = 1
        copied_q = deque(q)
        num_safe_blocks = num_empty_spaces - 3
        while copied_q:
            r, c = copied_q.popleft()
            for i, j in dir:
                dr, dc = r + i, c + j
                if 0 <= dr < n and 0 <= dc < m and copied_grid[dr][dc] == 0:
                    copied_grid[dr][dc] = 2
                    num_safe_blocks -= 1
                    copied_q.append((dr, dc))
        max_num_safe_blocks = max(max_num_safe_blocks, num_safe_blocks)
    
    print(max_num_safe_blocks)
    
    return None


if __name__ == '__main__':
    solve()