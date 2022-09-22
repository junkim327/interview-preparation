'''
    16926 - 배열 돌리기 1, https://www.acmicpc.net/problem/16926

    A[0][0] ← A[0][1] ← A[0][2] ← A[0][3] ← A[0][4]
        ↓                                       ↑
    A[1][0]   A[1][1] ← A[1][2] ← A[1][3]   A[1][4]
        ↓         ↓                   ↑         ↑
    A[2][0]   A[2][1] → A[2][2] → A[2][3]   A[2][4]
        ↓                                       ↑
    A[3][0] → A[3][1] → A[3][2] → A[3][3] → A[3][4]
'''

def main():
    n, m, r = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    groups = []

    for k in range(min(n, m) // 2):
        group = []
        for j in range(k, m-k):
            group.append(a[k][j])
            
        for i in range(k+1,n-k-1):
            group.append(a[i][m-k-1])
            
        for j in range(m-k-1,k - 1,-1):
            group.append(a[n-k-1][j])
            
        for i in range(n-k-2,k,-1):
            group.append(a[i][k])
            
        groups.append(group)

    for k in range(min(n, m) // 2):
        group = groups[k]
        l = len(group)
        index = r % l
        for j in range(k, m - k):
            a[k][j] = group[index]
            index = (index + 1) % l
        for i in range(k + 1, n - k - 1):
            a[i][m - k - 1] = group[index]
            index = (index + 1) % l
        for j in range(m - k - 1, k - 1, -1):
            a[n - k - 1][j] = group[index]
            index = (index + 1) % l
        for i in range(n - k - 2, k, -1):
            a[i][k] = group[index]
            index = (index + 1) % l
    
    for row in a:
        print(' '.join(map(str, row)))

    return

if __name__ == '__main__':
    main()
