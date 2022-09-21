'''
    16935 - 배열 돌리기 3, https://www.acmicpc.net/problem/16935
    
    1) 상하 반전, b[i][j] = a[n - 1 - i][j]
    2) 좌우 반전, b[i][j] = a[i][m - 1 - j]
    3) Rotate clockwise, b[i][j] = a[j][m - 1 - i]

'''

def main():

    def rotate_array(op_num, n, m):
        b = [[0] * m for _ in range(n)]

        if op_num == 1:
            for i in range(n):
                for j in range(m):
                    b[i][j] = a[n - i - 1][j]
        elif op_num == 2:
            for i in range(n):
                for j in range(m):
                    b[i][j] = a[i][m - j - 1]
        elif op_num == 3:
            b = [[0] * n for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    b[i][j] = a[n - j - 1][i]
        elif op_num == 4:
            b = [[0] * n for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    b[i][j] = a[j][m - i - 1]
        elif op_num == 5:
            for i in range(n//2):
                for j in range(m//2):
                    b[i][j + m//2] = a[i][j]
                    b[i + n//2][j + m//2] = a[i][j + m//2]
                    b[i + n//2][j] = a[i + n//2][j + m//2]
                    b[i][j] = a[i + n//2][j]
        elif op_num == 6:
            for i in range(n//2):
                for j in range(m//2):
                    b[i + n//2][j] = a[i][j]
                    b[i][j] = a[i][j + m//2]
                    b[i][j + m//2] = a[i + n//2][j + m//2]
                    b[i + n//2][j + m//2] = a[i + n//2][j]

        return b

    
    n, m, r = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    for op in map(int, input().split()):
        a = rotate_array(op, len(a), len(a[0]))
    for row in a:
        print(*row, sep=' ')

    return


if __name__ == '__main__':
    main()