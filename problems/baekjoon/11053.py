# 11053 - 가장 긴 증가하는 부분 수열, https://www.acmicpc.net/problem/11053

n = int(input()) # length
seq = list(map(int, input().split())) # sequence
cur_max_len = [1] * n

for i in range(n):
    for j in range(i):
        if seq[j] < seq[i]:
            cur_max_len[i] = max(cur_max_len[i], cur_max_len[j] + 1)

print(max(cur_max_len))