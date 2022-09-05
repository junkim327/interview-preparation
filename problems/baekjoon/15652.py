# 15652 - N과 M(4), https://www.acmicpc.net/problem/15652
N, M = map(int, input().split())
seq = [0] * M

def find_num(index, start, N, M):
    if index == M:
        print(' '.join(map(str, seq)))
        return
    
    for i in range(start, N+1):
        seq[index] = i
        find_num(index+1, i, N, M)

find_num(0, 1, N, M)