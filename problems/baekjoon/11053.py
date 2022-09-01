# 11053 - 가장 긴 증가하는 부분 수열, https://www.acmicpc.net/problem/11053

n = int(input()) # length
seq = list(map(int, input().split())) # sequence
longest_len = [1] * n

for i in range(n):
    for j in range(i):
        if seq[j] < seq[i]:
            longest_len[i] = max(longest_len[i], longest_len[j] + 1)

print(max(longest_len))