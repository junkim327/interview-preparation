# 1707 - 이분 그래프, https://www.acmicpc.net/problem/1707

import sys

def main():
    sys.setrecursionlimit(1000000)
    k = int(sys.stdin.readline())
    for _ in range(k):
        v, e = map(int, sys.stdin.readline().split())
        adjacent_list = [[] for _ in range(v)]
        group = [0] * v # 0: no group, 1: group 1, 2: group 2
        for _ in range(e):
            u, v = map(int, sys.stdin.readline().split())
            adjacent_list[u - 1].append(v - 1)
            adjacent_list[v - 1].append(u - 1)

        res = True
        for i in range(v):
            if group[i] == 0:
                if not dfs(i, 1, adjacent_list, group):
                    res = False
        print('YES' if res else 'NO')

def dfs(node, category, adjacent_list, group):
        group[node] = category
        for v in adjacent_list[node]:
            if group[v] == 0:
                if not dfs(v, 3 - category, adjacent_list, group):
                    return False
            elif group[node] == group[v]:
                return False
        return True

if __name__ == '__main__':
    main()