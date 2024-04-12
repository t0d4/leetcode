class Solution:
    def convert(self, s: str, numRows: int) -> str:
        mat = [[] for _ in range(numRows)]
        direction = 1 if numRows != 1 else 0
        current_row = 0
        for char in s:
            mat[current_row].append(char)
            current_row += direction
            if current_row == 0 or current_row == numRows - 1:
                direction *= -1
        return "".join(["".join(row) for row in mat])
