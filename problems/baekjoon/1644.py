# 1644 - 소수의 연속합, https://www.acmicpc.net/problem/1644

def solve():

    def prime_list(n):
        sieve = [False] * (n + 1)
        primes = []
        for i in range(2, n + 1):
            if sieve[i]:
                continue
            primes.append(i)
            j = i * 2
            while j <= n:
                sieve[j] = True
                j += i

        return primes
    
    n = int(input())
    primes = prime_list(n)
    l = r = 0
    sum = 0 if len(primes) == 0 else primes[0]
    ans = 0

    while l <= r and r < len(primes):
        if sum <= n:
            if sum == n:
                ans += 1
            r += 1
            if r < len(primes):
                sum += primes[r]
        else:
            sum -= primes[l]
            l += 1
    
    print(ans)

    return None


if __name__ == '__main__':
    solve()