# 11724 - 연결 요소의 개수, https://www.acmicpc.net/problem/11724
import sys

def main():
    sys.setrecursionlimit(100000)
    n, m = map(int, input().split()) # n -> number of vertices, m -> number of edges
    adjacent_list = [[] for _ in range(n + 1)]
    check = [False] * (n + 1)
    for _ in range(m):
        u, v = map(int, input().split())
        adjacent_list[u].append(v)
        adjacent_list[v].append(u)
    
    num_connected = 0
    for i in range(1, n + 1):
        if not check[i]:
            dfs(i, adjacent_list, check)
            num_connected += 1
    print(num_connected)

    return

def dfs(x, adjacent_list, check):
    check[x] = True
    for e in adjacent_list[x]:
        if not check[e]:
            dfs(e, adjacent_list, check)

if __name__ == '__main__':
    main()