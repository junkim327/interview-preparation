'''
    2193 - 이친수, https://www.acmicpc.net/problem/2193

    이친수의 condition:
        1. 0으로 시작하지 않음
        2. 1이 두 번 연속으로 나타나지 않음
    input: N (1<=N<=90) => 자리 수를 의미
    output: 이친수의 개수

    ex) input: 3, output: 2

    점화식: A[i][j], i: 자리 수(1<=i<=90), j: 마지막 숫자(0 or 1)
            A[i][j] = i 자리 수의 마지막 숫자가 j인 이친수의 개수
            A[i][0] = A[i-1][0] + A[i-1][1], A[i][1] = A[i-1][0]
'''

n = int(input()) # 이천수의 길이
a = [[0 for _ in range(2)] for _ in range(n + 1)]
a[1][1] = 1 # 초기 값 설정

for i in range(2, n + 1):
    a[i][0] = a[i-1][0] + a[i-1][1]
    a[i][1] = a[i-1][0]

print(sum(a[n]))

'''
1d array solution

점화식: A[N] = A[N-1] + A[N-2]

n = int(input()) # 이천수의 길이
a = [0] * (n + 1)
a[1] = 1 # 초기 값 설정

for i in range(2, n + 1):
    a[i] = a[i-1] + a[i-2]

print(a[n])
'''