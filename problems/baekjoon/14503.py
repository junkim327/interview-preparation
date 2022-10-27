'''
14503 - 로봇 청소기, https://www.acmicpc.net/problem/14503

1. 현재 위치를 청소한다.
2. 현재 위치에서 현재 방향을 기준으로 왼쪽방향부터 차례대로 탐색을 진행한다.
    - 1 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
    - 2 왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고 2번으로 돌아간다.
    - 3 네 방향 모두 청소가 이미 되어있거나 벽인 경우에는, 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
    - 4 네 방향 모두 청소가 이미 되어있거나 벽이면서, 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다.
'''

def main():
    n, m = map(int,input().split())
    r, c, d = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    while True:
        if a[r][c] == 0:
            # 1. 현재 위치를 청소
            a[r][c] = 2
            cnt += 1
        if a[r+1][c] != 0 and a[r-1][c] != 0 and a[r][c+1] != 0 and a[r][c-1] != 0:
            if a[r-dx[d]][c-dy[d]] == 1:
                break
            else:
                r -= dx[d]
                c -= dy[d]
        else:
            # 북 -> 서, 서 -> 남, 남 -> 동, 동 -> 북
            # 0 -> 3, 3 -> 2, 2 -> 1, 1 -> 0
            # (d - 1) % 4로 하면 d가 0일 경우 -1이 나오므로 +4 해주기
            d = (d + 3) % 4
            if a[r+dx[d]][c+dy[d]] == 0:
                r += dx[d]
                c += dy[d]
    
    print(cnt)

    return


if __name__ == '__main__':
    main()