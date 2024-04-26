class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []

        def dfs(s: str, n_open: int, n_close: int):
            if len(s) == 2 * n:
                res.append(s)
                return
            if n_open < n:
                dfs(s + "(", n_open + 1, n_close)
            if n_open > n_close:
                dfs(s + ")", n_open, n_close + 1)

        dfs("", 0, 0)
        return res
