# 77 - Combinations, https://leetcode.com/problems/combinations/description/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        a = []
        
        def solve(comb, idx):
            if len(comb) == k:
                a.append(comb)
                return

            for i in range(idx, n+1):
                solve(comb + [i], i + 1)


        solve([], 1)

        return a