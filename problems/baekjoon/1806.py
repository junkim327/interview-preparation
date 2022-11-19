# 1806 - 부분합, https://www.acmicpc.net/problem/1806

def solve():
    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    ans = n + 1
    l = r = 0
    partial_sum = a[0]

    while l <= r and r < n:
        if partial_sum < s:
            r += 1
            if r < n:
                partial_sum += a[r]
        if partial_sum >= s:
            ans = min(ans, r - l + 1)
            partial_sum -= a[l]
            l += 1
            if l > r and l < n:
                r = l
                partial_sum = a[l]



    if ans == n + 1:
        print(0)
    else:
        print(ans)
    

    return None


if __name__ == '__main__':
    solve()