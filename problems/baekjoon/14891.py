# 15662 - 톱니바퀴, https://www.acmicpc.net/problem/14891

from collections import deque

def main():

    def rotate_left(n, d, z):
        if n == -1 or a[n][2] == z:
            return
        rotate_left(n-1, -d, a[n][6])
        a[n].rotate(d)

    def rotate_right(n, d, z):
        if n == len(a) or a[n][6] == z:
            return
        rotate_right(n+1, -d, a[n][2])
        a[n].rotate(d)
        
    # num wheel
    t = 4
    a  = [deque(map(int, input())) for _ in range(t)] # N:0, S:1
    k = int(input())
    for _ in range(k):
        wheel_num, direction = map(int, input().split())
        rotate_left(wheel_num-2, -direction, a[wheel_num-1][6])
        rotate_right(wheel_num, -direction, a[wheel_num-1][2])
        a[wheel_num-1].rotate(direction)

    res = 0
    for i in range(4):
        if a[i][0] == 1:
            res += 2 ** i
    print(res)

    return

if __name__ == '__main__':
    main()