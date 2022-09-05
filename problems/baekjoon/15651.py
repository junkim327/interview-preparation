# 15651 - N과 M(3), https://www.acmicpc.net/problem/15651
N, M = map(int, input().split())
seq = [0] * M

def find_num(index, N, M):
    if index == M:
        print(' '.join(map(str, seq)))
        return
    
    for i in range(1, N+1):
        seq[index] = i
        find_num(index+1, N, M)

find_num(0, N, M)