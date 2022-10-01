'''
    14888 - 연산자 끼워넣기, https://www.acmicpc.net/problem/14888

    
'''


def main():
    n = int(input())
    a = list(map(int, input().split()))
    plus, minus, mul, div = map(int, input().split())
    res = []

    def solve(i, cur, plus, minus, mul, div):
        nonlocal n
        if i == n:
            res.append(cur)
            return

        if plus > 0:
            solve(i + 1, cur + a[i], plus - 1, minus, mul, div)
        if minus > 0:
            solve(i + 1, cur - a[i], plus, minus - 1, mul, div)
        if mul > 0:
            solve(i + 1, cur * a[i], plus, minus, mul - 1, div)
        if div > 0:
            if cur >= 0:
                solve(i + 1, cur // a[i], plus, minus, mul, div - 1)
            else:
                solve(i + 1, -(-cur // a[i]), plus, minus, mul, div - 1)

        
    solve(1, a[0], plus, minus, mul, div)

    print(max(res))
    print(min(res))

        
    return


if __name__ == '__main__':
    main()