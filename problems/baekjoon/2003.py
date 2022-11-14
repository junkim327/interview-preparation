# 2003 - 수들의 합 2, https://www.acmicpc.net/problem/2003

def solve():
    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    l = r = 0
    sum = a[0]
    ans = 0

    while l <= r and r < n:
        if sum < s:
            r += 1
            if r < n:
                sum += a[r]
        elif sum == s:
            ans += 1
            r += 1
            if r < n:
                sum += a[r]
        elif sum > s:
            sum -= a[l]
            l += 1
            if l > r and l < n:
                r = l
                sum = a[l]
    
    print(ans)
    
    return None


if __name__ == '__main__':
    solve()