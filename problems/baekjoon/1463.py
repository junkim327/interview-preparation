# 1463 - 1로 만들기, https://www.acmicpc.net/problem/1463
'''
Top-Down Solution

import sys
sys.setrecursionlimit(10000000)

def top_down(n, a):
    if a[n] != 0 or n == 1:
        return a[n]
    
    sum = 1 + get_num_operations(n-1, a)
    if n % 3 == 0:
        sum = min(sum, 1 + get_num_operations(n//3, a))
    if n % 2 == 0:
        sum = min(sum, 1 + get_num_operations(n//2, a))
    
    a[n] = sum
    
    return sum
'''

# Bottom-Up Solution

n = int(input())
a = [0] * (n + 1)
a[1] = 0 # initialize explicitly in case the array is not initialized with zeros
for i in range(2, n+1):
    a[i] = a[i-1] + 1
    if i % 2 == 0:
        a[i] = min(a[i], a[i//2] + 1)
    if i % 3 == 0:
        a[i] = min(a[i], a[i//3] + 1)
print(a[n])