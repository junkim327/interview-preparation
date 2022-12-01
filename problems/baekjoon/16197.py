# 16197 - 두 동전, https://www.acmicpc.net/problem/16197

def main():
    n, m = map(int, input().split())
    coins = []
    a = []
    for i in range(n):
        row = []
        for j, c in enumerate(input()):
            row.append(c)
            if c == 'o':
                coins.append((i, j))
        a.append(row)
    
    button = [(1, 0), (0, -1), (0, 1), (-1, 0)]

    def is_out_of_bounds(x, y):
        return True if x < 0 or x >= n or y < 0 or y >= m else False

    def push(coin1, coin2, cnt):
        if cnt > 10:
            return -1
        
        is_c1_out_of_bounds = is_out_of_bounds(coin1[0], coin1[1])
        is_c2_out_of_bounds = is_out_of_bounds(coin2[0], coin2[1])
        if is_c1_out_of_bounds and is_c2_out_of_bounds:
            return -1
        if is_c1_out_of_bounds != is_c2_out_of_bounds:
            return cnt

        ans = -1
        for direction in button:
            c1_i, c1_j = coin1[0] + direction[0], coin1[1] + direction[1]
            c2_i, c2_j = coin2[0] + direction[0], coin2[1] + direction[1]
            if not is_out_of_bounds(c1_i, c1_j) and a[c1_i][c1_j] == '#':
                c1_i, c1_j = coin1[0], coin1[1]
            if not is_out_of_bounds(c2_i, c2_j) and a[c2_i][c2_j] == '#':
                c2_i, c2_j = coin2[0], coin2[1]

            temp = push((c1_i, c1_j), (c2_i, c2_j), cnt + 1)
            if temp == -1: continue
            if ans == -1 or temp < ans:
                ans = temp

        return ans
       
    print(push(coins[0], coins[1], 0))
       
    return


if __name__ == '__main__':
    main()