'''
    1309 - 동물원, https://www.acmicpc.net/problem/1309

    점화식:
        D[i][0] = i칸에 사자를 배치하지 않았을 때의 경우의 수 = D[i-1][0] + D[i-1][1]
        D[i][1] = i칸에 사자를 배치했을 때의 경우의 수 = D[i-1][0] * 2 + D[i - 1][1]
        최종 점화식 = sum(D[i])
'''

def main():
    n = int(input())
    d = [[0, 0] for _ in range(n)]
    print(solution(n, d))

    return

def solution(n, d):
    mod = 9901
    d[0][0], d[0][1] = 1, 2
    for i in range(1, n):
        d[i][0] = d[i - 1][0] + d[i - 1][1] % mod
        d[i][1] = (d[i - 1][0]*2 + d[i - 1][1]) % mod

    return sum(d[n - 1]) % mod

if __name__ == '__main__':
    main()