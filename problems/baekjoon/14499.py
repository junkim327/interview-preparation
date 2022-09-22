'''
    14499 - 주사위 굴리기, https://www.acmicpc.net/problem/14499
      
                             East           West         North         South
    dice =>     0             0              0             1             3               
              4 1 5         3 4 1          1 5 3         4 2 5         4 0 5
                2             2              2             3             1
                3             5              4             0             2
            0 1 2 3 4 5 [0 4 2 5 3 1]   [0 5 2 4 1 3]  [1 2 3 0 4 5] [3 0 1 2 4 5]
'''

def main():

    move = [(0, 1), (0, -1), (-1, 0), (1, 0)]

    def roll_the_dice(x, y):
        dice = [0] * 6
        for c in commands:
            x_i, y_i = x + move[c - 1][0], y + move[c - 1][1]
            if 0 <= x_i < n and 0 <= y_i < m:
                if c == 1:
                    dice[1], dice[3], dice[4], dice[5] = dice[4], dice[5], dice[3], dice[1]
                elif c == 2:
                    dice[1], dice[3], dice[4], dice[5] = dice[5], dice[4], dice[1], dice[3]
                elif c == 3:
                    dice[0], dice[1], dice[2], dice[3] = dice[1], dice[2], dice[3], dice[0]
                elif c == 4:
                    dice[0], dice[1], dice[2], dice[3] = dice[3], dice[0], dice[1], dice[2]

                x, y = x_i, y_i
                if a[x][y] == 0:
                    a[x][y] = dice[3]
                else:
                    dice[3] = a[x][y]
                    a[x][y] = 0
                print(dice[1])

    n, m, x, y, k = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    commands = list(map(int, input().split()))

    roll_the_dice(x, y)

    return


if __name__ == '__main__':
    main()