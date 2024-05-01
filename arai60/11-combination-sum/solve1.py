from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combs = set()

        def dfs(n: int, comb: tuple):
            if n == target:
                combs.add(tuple(sorted(comb)))
            elif n > target:
                return
            else:
                for c in candidates:
                    dfs(n + c, comb + (c,))

        dfs(0, ())
        return list(combs)
