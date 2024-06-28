from collections import deque


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        n_row, n_col = len(grid), len(grid[0])
        visited = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def bfs(r: int, c: int):
            q = deque([])
            q.append((r, c))
            # `visited.add((r, c))` IS MISSING HERE
            while q:
                r, c = q.popleft()
                for r_res, c_res in directions:
                    row, col = r + r_res, c + c_res
                    if (
                        row in range(n_row)
                        and col in range(n_col)
                        and grid[row][col] == "1"
                        # `and (row, col) not in visited` IS MISSING HERE
                    ):
                        q.append((row, col))
                    visited.add((row, col))

        n_islands = 0
        r, c = 0, 0
        while r < n_row:
            while c < n_col:
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    n_islands += 1
                c += 1
            r += 1

        return n_islands
