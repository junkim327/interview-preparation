def GCD(a, b):
    if b == 0:
        return a
    else:
        return GCD(b, a%b)

a, b = map(int, input().split())
g = GCD(a, b)
print(g)
print(a*b//g)