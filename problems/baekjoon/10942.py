
import sys

read = sys.stdin.readline

def top_down():
    n = int(read())
    nums = list(map(int, read().split()))
    m = int(read().rstrip())
    dp = [[-1] * n for _ in range(n)]
    
    def is_palindrome(s, e):
        if dp[s][e] != -1:
            return dp[s][e]
        if s == e:
            dp[s][e] = 1
            return 1
        if s + 1 == e:
            if nums[s] == nums[e]:
                dp[s][e] = 1
                return 1
            else:
                dp[s][e] = 0
                return 0
        if nums[s] != nums[e]:
            dp[s][e] = 0
            return 0
        else:
            dp[s][e] = is_palindrome(s + 1, e - 1)
            return dp[s][e]
        
    for _ in range(m):
        s, e = map(int, read().split())
        print(is_palindrome(s - 1, e - 1))

    return None

if __name__ == '__main__':
    solve()