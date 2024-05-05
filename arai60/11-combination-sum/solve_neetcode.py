class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []

        def dfs(start_idx: int, cur: list[int], total: int):
            if total == target:
                res.append(cur.copy())
                return
            if start_idx >= len(candidates) or total > target:
                return

            cur.append(candidates[start_idx])
            dfs(start_idx, cur, total + candidates[start_idx])
            cur.pop()
            dfs(start_idx + 1, cur, total)

        dfs(0, [], 0)
        return res
