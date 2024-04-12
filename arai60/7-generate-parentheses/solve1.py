class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        # n = 1
        # ()
        # n = 2
        # (()), ()()
        # n = 3
        # ((())), (()()), (())(), ()(()), ()()()
        # every time we have 2 choices: 1. close immediately 2. close later
        if n == 1:
            return ["()"]
        res = []
        for pattern in self.generateParenthesis(n - 1):
            res.append("(" + pattern + ")")
            res.append("()" + pattern)
            res.append(pattern + "()")
        return list(set(res))


s = Solution()
res = s.generateParenthesis(4)
print(
    set(res)
    ^ set(
        [
            "(((())))",
            "((()()))",
            "((())())",
            "((()))()",
            "(()(()))",
            "(()()())",
            "(()())()",
            "(())(())",
            "(())()()",
            "()((()))",
            "()(()())",
            "()(())()",
            "()()(())",
            "()()()()",
        ]
    )
)
