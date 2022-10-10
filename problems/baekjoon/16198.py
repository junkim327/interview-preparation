# 16198 - 에너지 모으기, https://www.acmicpc.net/problem/16198

def main():
    n = int(input())
    w = list(map(int, input().split()))

    def gather_energy(a):
        n = len(a)
        if n == 2:
            return 0
        ans = 0
        for i in range(1, n-1):
            energy = a[i-1] * a[i+1]
            b = a[:i] + a[i+1:]
            energy += gather_energy(b)
            if ans < energy:
                ans = energy
        return ans

    print(gather_energy(w))
    return

if __name__ == '__main__':
    main()