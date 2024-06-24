class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []

        def dfs(s: str, n_open: int, n_close: int):
            if n_open == n and n == n_close:
                res.append(s)
                return
            # NOTE: 以下の2つのif文は片方をelifにしてはいけない！（片方をelifにしたら((()))みたいなやつしか作れなくなる。）
            if n_open < n:
                dfs(s + "(", n_open + 1, n_close)
            if n_open > n_close:
                dfs(s + ")", n_open, n_close + 1)

        dfs("", 0, 0)
        return res
