# 10819 - 차이를 최대로, https://www.acmicpc.net/problem/10819

"""
solution 1 - 76ms
first sort the array. ex) 4 15 9 17 6 => 4 6 9 15 17

index: 0 1 2 3  4     |   2 3  0 4  1  =>  the index of elements which maximizes sum
array: 4 6 9 15 17    |   9 15 4 17 6  => |9 - 15| + |15 - 4| + |4 - 17| + |17 - 6| = 6 + 11 + 13 + 11 = 41

make two pointers, i starts at 0 and j starts at middle of the index.

i     j                             i     j                                  i   j(out of index)
0 1 2 3 4      =>                 0 1 2 3 4            =>                0 1 2 3 4
|a[j] - a[i]|  +  |a[i-1 = 0] - a[j]| + |a[j] - a[i]|  +   max(|a[i-1] - a[i]|, |a[i] - a[i+1]|)
|15 - 4|  +  |4 - 17| + |17 - 6| + max(|6 - 9|, |9 - 15|) = 41
"""
"""
N = int(input())
a = list(map(int, input().split()))
a.sort()

i = 0
j = (N//2) if N%2==0 else (N//2+1)

sum = 0
while j < N:
    if (i-1) >= 0:
        sum += abs(a[j] - a[i-1])
    sum += abs(a[j] - a[i])
    j += 1
    i += 1

if N%2!=0: sum += max(abs(a[i] - a[i-1]), abs(a[i] - a[i+1]))
print(sum)
"""

"""
Solution 2
"""
def next_permutation(a, n):
    i = n - 1
    while i > 0 and a[i-1] >= a[i]: i -= 1
    if i == 0: return False
    j = n - 1
    while a[j] <= a[i-1]: j -= 1
    a[i-1], a[j] = a[j], a[i-1]
    j = n - 1
    while (i < j):
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1

    return True

def calculate(a):
    sum = 0
    for i in range(1, len(a)):
        sum += abs(a[i-1] - a[i])
    return sum

N = int(input())
a = list(map(int, input().split()))
a.sort()
ans = 0
while True:
    temp = calculate(a)
    ans = max(ans, temp)
    if not next_permutation(a, N):
        break
print(ans)