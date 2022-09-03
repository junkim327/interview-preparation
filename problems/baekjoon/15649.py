# 15649 - N과 M(1), https://www.acmicpc.net/problem/15649
N, M = map(int, input().split())
num_used = [False] * (N + 1)
sequence = [0] * M

def find_num(index, N, M):
    if index == M:
        print(' '.join(map(str, sequence)))
        return
    
    for i in range(1, N+1):
        if num_used[i]: continue
        num_used[i] = True
        sequence[index] = i
        find_num(index+1, N, M)
        num_used[i] = False

find_num(0, N, M)