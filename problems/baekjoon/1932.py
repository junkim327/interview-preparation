'''
    1932 - 정수 삼각형, https://www.acmicpc.net/problem/1932 

    점화식: d


        00
    10       11
20      21       22
'''

def solve():
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    
    if n == 1:
        print(a[0][0])
        return None

    for i in range(1, n):
        for j in range(i+1):
            # check upper left side
            if j == 0:
                a[i][j] += a[i-1][j]
            elif j == i:
                a[i][j] += a[i-1][j-1]
            else:
                a[i][j] += max(a[i-1][j], a[i-1][j-1])

    print(max(a[n-1]))
    return None


if __name__ == '__main__':
    solve()