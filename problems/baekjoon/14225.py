# 14225 - 부분수열의 합, https://www.acmicpc.net/problem/14225

import sys

read = sys.stdin.readline

def recursive():
    S = int(read())
    a = list(map(int, read().rstrip().split()))
    sum_dict = {}

    def recursive(index, cur_sum):
        if index == S:
            sum_dict[cur_sum] = 1
            return None
        
        recursive(index + 1, cur_sum + a[index])
        recursive(index + 1, cur_sum)

        return None

    recursive(0, 0)
    
    i = 1
    while True:
        if sum_dict.get(i, 0) == 0:
            print(i)
            break
        i += 1

    return None

def simple_solution():
    read()
    a = 0
    for i in [*sorted(map(int, read.split()))]:
        if a + 1 < i:
            break
        a += i
    print(a + 1)

if __name__ == '__main__':
    recursive()
    # simple_solution()