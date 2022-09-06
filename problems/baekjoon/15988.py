'''
    15988 - 1,2,3 더하기 3, https://www.acmicpc.net/problem/15988
    
    점화식: D[N] = D[N-1] + D[N-2] + D[N-3]

    #1에서 mod로 나눠주려 했더니 solution()이 너무 느려짐 그래서 #2 에서 mod로 나눠줌
'''

def main():
    d = [0] * (1000000 + 1)
    d[0] = 1
    solution(d)

    t = int(input())
    for _ in range(t):
        n = int(input())
        print(d[n]) # 1

    return

def solution(d):
    mod = 1000000009
    for i in range(1, 1000000 + 1):
        if i - 1 >= 0:
            d[i] += d[i - 1]
        if i - 2 >= 0:
            d[i] += d[i - 2]
        if i - 3 >= 0:
            d[i] += d[i - 3]
        d[i] %= mod # 2

    return

if __name__ == '__main__':
    main()