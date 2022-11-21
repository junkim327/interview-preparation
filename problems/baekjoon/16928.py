# 16928 - 뱀과 사다리 게임, https://www.acmicpc.net/problem/16928

from collections import deque

def solve():
    n, m = map(int, input().split())
    snakes_and_ladders_dict = {k: v for k, v in list(map(int, input().split()) for _ in range(n + m))}

    d = [-1] * 101
    d[1] = 0
    q = deque()
    q.append(1)
    while q:
        block = q.popleft()
        for step in range(1, 7):
            next_block = snakes_and_ladders_dict.setdefault(block + step, block + step)
            if next_block == 100:
                print(d[block] + 1)
                return
            
            if next_block < 100 and d[next_block] == -1:
                q.append(next_block)
                d[next_block] = d[block] + 1

    print(d[100])
    return None


if __name__ == '__main__':
    solve()