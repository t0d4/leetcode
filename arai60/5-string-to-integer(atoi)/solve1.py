class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s:
            return 0
        start_idx = 0
        negative = False
        if s[0] == "-":
            negative = True
            start_idx = 1
        elif s[0] == "+":
            start_idx = 1
        elif s[0].isdigit():
            pass
        else:
            # invalid. no more digits can be read.
            return 0
        res = []
        for char in s[start_idx:]:
            if char.isdigit():
                res.append(char)
            else:
                break
        if not res:
            return 0
        L_BOUND = -(2**31)
        U_BOUND = 2**31 - 1
        converted = int("".join(res)) * (-1 if negative else 1)
        if L_BOUND <= converted <= U_BOUND:
            return converted
        elif converted < L_BOUND:
            return L_BOUND
        else:
            return U_BOUND
