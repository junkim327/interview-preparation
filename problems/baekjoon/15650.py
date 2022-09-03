# 15649 - N과 M(2), https://www.acmicpc.net/problem/15650
N, M = map(int, input().split())
num_used = [False] * (N + 1)
sequence = [0] * M

def find_num(index, start, N, M):
    if index == M:
        print(' '.join(map(str, sequence)))
        return
    
    for i in range(start, N+1):
        sequence[index] = i
        find_num(index+1, i + 1, N, M)

find_num(0, 1, N, M)
