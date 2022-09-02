'''
    1912 - 연속합, https://www.acmicpc.net/problem/1912

    점화식: D[i] = i번째 수가 연속된 부분 수열의 마지막 숫자일때 가장 큰 합
                = max(A[i] + D[i-1], A[i])
'''

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(solution(n, a))
    return

def solution(n, a):
    cur_max_sum = list(a)
    for i in range(1, n):
        cur_max_sum[i] = max(a[i] + cur_max_sum[i-1], a[i])
    return max(cur_max_sum)


if __name__ == "__main__":
    main()