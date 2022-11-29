'''
    16974 - 레벨 햄버거, https://www.acmicpc.net/problem/16974
'''

import sys

read = sys.stdin.readline

def solve():
    N, X = map(int, read().rstrip().split())
    burger_height = [0] * N
    burger_height[0] = 1
    for i in range(1, N):
        burger_height[i] = burger_height[i - 1] * 2 + 3
    
    num_patty_list = [0] * N
    num_patty_list[0] = 1
    for i in range(1, N):
        num_patty_list[i] = num_patty_list[i - 1] * 2 + 1
    
    def get_num_eaten_patty(level, x):
        if level == 0:
            if x > 0:
                return 1
            else:
                return 0
        
        if x == 1:
            return 0
        elif 1 < x <= 1 + burger_height[level - 1]:
            return get_num_eaten_patty(level - 1, x - 1)
        elif x == 1 + burger_height[level - 1] + 1:
            return num_patty_list[level - 1] + 1
        elif 1 + burger_height[level - 1] + 1 < x <= 2 + burger_height[level - 1] * 2:
            return num_patty_list[level - 1] + 1 + get_num_eaten_patty(level - 1, x - 1 - burger_height[level - 1] - 1)
        elif x == 3 + burger_height[level - 1] * 2:
            return num_patty_list[level - 1] * 2 + 1
        
    print(get_num_eaten_patty(N, X))

    return None

if __name__ == '__main__':
    solve()