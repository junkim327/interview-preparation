# 6603 - 로또, https://www.acmicpc.net/problem/6603

def main():

    def solve(s, index, lotto):
        if len(lotto) == 6:
            print(' '.join(map(str, lotto)))
            return
        if index == len(s):
            return
        solve(s, index + 1, lotto + [s[index]])
        solve(s, index + 1, lotto)


    while True:
        k, *s = list(map(int, input().split()))
        if k == 0:
            break
        solve(s, 0, [])
        print()

    return


if __name__ == '__main__':
    main()