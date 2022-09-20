# 13913 - 숨바꼭질 4, https://www.acmicpc.net/problem/13913

from collections import deque

def main():

    a_idx, b_idx = map(int, input().split())
    if b_idx <= a_idx:
        print(a_idx - b_idx)
        route = ''
        for i in range(a_idx, b_idx - 1, -1):
            print(str(i), end=' ')
        print(route)
        return

    max_len = b_idx * 2
    check = [False] * max_len
    axis = [-1] * max_len

    q = deque()
    q.append(a_idx)
    check[a_idx] = True

    while q:
        cur_idx = q.popleft()
        for next_idx in [cur_idx - 1, cur_idx + 1, cur_idx * 2]:
            if next_idx == b_idx:
                count = 0
                axis[next_idx] = cur_idx
                route = str(next_idx)
                while axis[b_idx] != -1:
                    route = str(axis[b_idx]) + ' ' + route
                    b_idx = axis[b_idx]
                    count += 1
                print(count)
                print(route)
                return

            if 0 <= next_idx < max_len and check[next_idx] == False:
                q.append(next_idx)
                axis[next_idx] = cur_idx
                check[next_idx] = True

    return


if __name__ == '__main__':
    main()