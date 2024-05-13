from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []

        def dfs(start_idx: int, cur: list[int], cur_sum: int):
            if cur_sum == target:
                res.append(cur.copy())
                return
            if cur_sum > target or start_idx >= len(
                candidates
            ):  # REF `or start_idx >= len(candidates):` part
                return
            cur.append(candidates[start_idx])  # REF
            dfs(start_idx, cur, cur_sum + candidates[start_idx])
            cur.pop()  # REF
            dfs(start_idx + 1, cur, cur_sum)

        dfs(0, [], 0)
        return res
