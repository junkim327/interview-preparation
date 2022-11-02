'''
    11057 - 오르막 수, https://www.acmicpc.net/problem/11057

    점화식: a[n][d] = 수의 길이가 n이고 마지막 자리 수가 d일때 오르막 수의 개수
           a[n][d] += a[n-1][i] for i in 0 to d
'''


def main():
    n = int(input())
    a = [[0] * 10 if i != 1 else [1] * 10 for i in range(n + 1)]
    mod = 10007

    if n == 1:
        print(10)
        return
    
    for i in range(2, n + 1):
        for j in range(10):
            for k in range(j + 1):
                a[i][j] += a[i-1][k]
                a[i][j] %= mod

    print(sum(a[n]) % mod)
    return

def solve2():
    n = int(input())
    a = [1] * 10
    for i in range(1, n):
        for j in range(1, 10):
            a[j] += a[j-1]
    
    print(sum(a) % 10007)

    return None
    

if __name__ == '__main__':
    #main()
    solve2()