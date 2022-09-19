# 1697 - 숨바꼭질, https://www.acmicpc.net/problem/1697

from collections import deque

def main():
    a_idx, b_idx = map(int, input().split()) # a: 수빈, b: 동생
    if b_idx <= a_idx: 
        print(a_idx - b_idx)
        return

    max_len = b_idx * 2
    location = [-1] * max_len
    q = deque()
    q.append(a_idx)
    location[a_idx] = 0 # start point
    while q:
        cur_idx = q.popleft()
        for next_idx in [cur_idx - 1, cur_idx + 1, cur_idx * 2]:
            if next_idx == b_idx:
                print(location[cur_idx] + 1)
                return
            if 0 <= next_idx < max_len and location[next_idx] == -1:
                q.append(next_idx)
                location[next_idx] = location[cur_idx] + 1

    return

if __name__ == '__main__':
    main()