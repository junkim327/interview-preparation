import sys

n = 9
dwarfs = [int(input()) for _ in range(n)]
height_sum = sum(dwarfs)

dwarfs.sort()

for i in range(len(dwarfs)):
    for j in range(i+1, len(dwarfs)):
        if (height_sum - dwarfs[i] - dwarfs[j]) == 100:
            for k in range(0, n):
                if i == k or j == k:
                    continue
                print(dwarfs[k])
            sys.exit(0)
