# 10844 - 쉬운 계단 수, https://www.acmicpc.net/problem/10844

'''
condition: 인접한 모든 자리의 차이가 1이다. 0으로 시작하는 수는 계단 수가 아니다.
input: N = 계단 길이, 1 <= N <= 100
output: 총 계단 수
점화식: A[i][j] = 길이 i인 계단의 마지막 숫자가 j인 계단의 수 
               = A[i-1][j-1] + A[i-1][j+1], if 1 <= j <= 8
               = A[i-1][j+1], if j == 0
               = A[i-1][j-1], if j == 9

'''

n = int(input()) # 계단 길이
mod = 1000000000 # 나중에 정답을 나눌 수
a = [[0 for _ in range(10)] for _ in range(n + 1)]
for i in range(1, 10):
    a[1][i] = 1

for i in range(2, n + 1):
    for j in range(0, 10):
        if j-1 >= 0: 
            a[i][j] += a[i-1][j-1]
        if j+1 <= 9:
            a[i][j] += a[i-1][j+1]

print(sum(a[n]) % mod)