'''
    1149 - RGB 거리, https://www.acmicpc.net/problem/1149

    점화식: D[i][j] = i번 집을 j번 색으로 칠하는 비용
        1) D[i][빨] = min(D[i-1][파], D[i-1][초]) + D[i][빨]
        1) D[i][초] = min(D[i-1][파], D[i-1][빨]) + D[i][초]
        1) D[i][파] = min(D[i-1][빨], D[i-1][초]) + D[i][파]
'''

def main():
    n = int(input())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))
    
    print(solution(n, a))
    return

def solution(n, a):
    for i in range(1, n):
        a[i][0] += min(a[i - 1][1], a[i - 1][2])
        a[i][1] += min(a[i - 1][0], a[i - 1][2])
        a[i][2] += min(a[i - 1][0], a[i - 1][1])

    return min(a[n - 1])

if __name__ == '__main__':
    main()