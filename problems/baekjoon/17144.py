# 17144 - 미세먼지 안녕!, https://www.acmicpc.net/problem/17144

import sys

read = sys.stdin.readline

def solve():
    dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def spread_dust(r, c):
        duplicated_grid = [row[:] for row in grid]
        for i in range(r):
            for j in range(c):
                count = 0
                if duplicated_grid[i][j] == -1:
                    continue
                # 확산한 방향의 개수
                elif duplicated_grid[i][j] != 0:
                    for x, y in dir:
                        dx, dy = i + x, j + y
                        if 0 <= dx < r and 0 <= dy < c and duplicated_grid[dx][dy] != -1:
                            # 확산
                            grid[dx][dy] += (duplicated_grid[i][j] // 5)
                            count += 1
                grid[i][j] -= (duplicated_grid[i][j] // 5) * count
                    
        return None
    
    def operate_air_purifier(r, c, index):
        top_r, top_c = index, 0
        bot_r, bot_c = index + 1, 0

        top_r -= 1
        while top_r > 0:
            grid[top_r][top_c] = grid[top_r - 1][top_c]
            top_r -= 1
        while top_c < c - 1:
            grid[top_r][top_c] = grid[top_r][top_c + 1]
            top_c += 1
        while top_r < index:
            grid[top_r][top_c] = grid[top_r + 1][top_c]
            top_r += 1
        while top_c > 0:
            grid[top_r][top_c] = grid[top_r][top_c - 1]
            top_c -= 1
        grid[top_r][top_c + 1] = 0

        bot_r += 1
        while bot_r < r - 1:
            grid[bot_r][bot_c] = grid[bot_r + 1][bot_c]
            bot_r += 1
        while bot_c < c - 1:
            grid[bot_r][bot_c] = grid[bot_r][bot_c + 1]
            bot_c += 1
        while bot_r > index + 1:
            grid[bot_r][bot_c] = grid[bot_r - 1][bot_c]
            bot_r -= 1
        while bot_c > 0:
            grid[bot_r][bot_c] = grid[bot_r][bot_c - 1]
            bot_c -= 1
        grid[bot_r][bot_c + 1] = 0

        return None
    
    R, C, T = map(int, read().rstrip().split())
    grid = [list(map(int, read().rstrip().split())) for _ in range(R)]
    purifier_idx = 0
    for i in range(R):
        if grid[i][0] == -1:
            purifier_idx = i
            break

    for i in range(T):
        spread_dust(R, C)
        operate_air_purifier(R, C, purifier_idx)
    
    dust_sum = sum(sum(row) for row in grid) + 2
    print(dust_sum)

    return None


if __name__ == '__main__':
    solve()