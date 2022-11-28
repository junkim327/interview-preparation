# 16939 - 2x2x2 큐브, https://www.acmicpc.net/problem/16939

import sys

read = sys.stdin.readline

def solve():
    cube_side = [
        [(1, 5), (3, 7), (5, 9), (7, 11), (9, 24), (11, 22), (22, 3), (24, 1)],
        [(2, 6), (4, 8), (6, 10), (8, 12), (10, 23), (12, 21), (21, 4), (23, 2)],
        [(13, 5), (14, 6), (5, 17), (6, 18), (17, 21), (18, 22), (21, 13), (22, 14)],
        [(15, 7), (16, 8), (7, 19), (8, 20), (19, 23), (20, 24), (23, 15), (24, 16)],
        [(3, 17), (4, 19), (17, 10), (19, 9), (10, 16), (9, 14), (14, 4), (16, 3)],
        [(1, 18), (2, 20), (18, 12), (20, 11), (12, 15), (11, 13), (13, 2), (15, 1)]
    ]

    def solve_cube(side, direction=0):
        temp = cube[:]
        solved = True
        if direction == 0:
            for r, c in side:
                temp[r - 1] = cube[c - 1]
        else:
            for c, r in side:
                temp[r - 1] = cube[c - 1]
        for i in range(0, len(cube), 4):
            s1, s2, s3, s4 = i, i + 1, i + 2, i + 3
            if temp[s1] != temp[s2] or temp[s2] != temp[s3] or temp[s3] != temp[s4]:
                solved = False
                break
        return solved

    cube = list(map(int, read().rstrip().split()))

    for side in cube_side:
        if solve_cube(side) or solve_cube(side, direction=1):
            print(1)
            return None
    
    print(0)
    return None

if __name__ == '__main__':
    solve()