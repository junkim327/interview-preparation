while True:
    try:
        n_real = int(input())
        real_divisor = list(map(int, input().split()))
    except:
        break

    N = min(real_divisor) * max(real_divisor)
    print(N)
    break