# 1182 - 부분수열의 합, https://www.acmicpc.net/problem/1182

def main():

    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0


    def solve(i, total):
        nonlocal ans
        if i == n:
            if total == s:
                ans += 1
            return
        
        solve(i + 1, total + a[i])
        solve(i + 1, total)


    solve(0, 0)
    if s == 0:
        ans -= 1
    print(ans)


    return


if __name__ == '__main__':
    main()