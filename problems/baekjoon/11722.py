# 11722 - 가장 긴 감소하는 부분 수열, https://www.acmicpc.net/problem/11722

n = int(input()) # sequence length
seq = list(map(int, input().split())) # sequence
cur_max_len = [1] * n # longest sequence length at i index

for i in range(n):
    for j in range(i):
        if seq[j] > seq[i]:
            cur_max_len[i] = max(cur_max_len[i], cur_max_len[j] + 1)

print(max(cur_max_len))
