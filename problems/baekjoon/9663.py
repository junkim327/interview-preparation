# 9663 - N-Queen, https://www.acmicpc.net/problem/9663

import sys

read = sys.stdin.readline

def solve():
    N = int(read())

    cols = set()
    pos_diag = set()
    neg_diag = set()
    
    def backtrack(r):
        if r == N:
            return 1

        ans = 0
        for c in range(N):
            if c in cols or (r + c) in pos_diag or (r - c) in neg_diag:
                continue

            cols.add(c)
            pos_diag.add(r + c)
            neg_diag.add(r - c)

            ans += backtrack(r + 1)

            cols.remove(c)
            pos_diag.remove(r + c)
            neg_diag.remove(r - c)
        
        return ans

    print(backtrack(0))
    
    return None

if __name__ == '__main__':
    solve()