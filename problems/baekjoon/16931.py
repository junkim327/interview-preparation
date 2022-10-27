# 16931 - 겉넓이 구하기, https://www.acmicpc.net/problem/16931

def main():
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]

    surface_area = 0
    for i in range(n):
        area = 0
        for j in range(m):  
            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]

                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    area += a[i][j]
                else:
                    if a[nx][ny] < a[i][j]:
                        area += a[i][j] - a[nx][ny]

        surface_area += area
    
    surface_area += n * m * 2
    print(surface_area)
            
    return


if __name__ == '__main__':
    main()
