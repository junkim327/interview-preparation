def is_prime(a):
    if a < 2: return False
    i = 2
    while i * i <= a:
        if a % i == 0:
            return False
        i += 1
    return True   

len = int(input())
nums = list(map(int, input().split()))
n_prime = 0

for n in nums:
    if is_prime(n):
        n_prime += 1

print(n_prime)