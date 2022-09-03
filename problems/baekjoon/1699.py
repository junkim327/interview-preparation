'''
    1699 - 제곱수의 합, https://www.acmicpc.net/problem/1699

    점화식: D[N] = min(D[N-i^2]) + 1
'''
def main():
    n = int(input())
    d = [0] * (n + 1)
    print(solution(n, d))
    return

def solution(n, d):
    for i in range(1, n + 1):
        d[i] = i
        j = 1
        while j * j <= i:
            if d[i] > d[i - j*j] + 1:
                d[i] = d[i - j*j] + 1
            j += 1
    return d[n]

if __name__ == '__main__':
    main()