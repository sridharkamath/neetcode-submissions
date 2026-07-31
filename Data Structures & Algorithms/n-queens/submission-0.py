class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for _ in range(n)]

        rows = set()
        diag = set()      # row - col
        anti = set()      # row + col

        res = []

        def dfs(c):
            if c == n:
                res.append(["".join(row) for row in board])
                return

            for r in range(n):

                if r in rows:
                    continue

                if (r - c) in diag:
                    continue

                if (r + c) in anti:
                    continue

                # Place queen
                board[r][c] = "Q"
                rows.add(r)
                diag.add(r - c)
                anti.add(r + c)

                dfs(c + 1)

                # Backtrack
                board[r][c] = "."
                rows.remove(r)
                diag.remove(r - c)
                anti.remove(r + c)

        dfs(0)
        return res