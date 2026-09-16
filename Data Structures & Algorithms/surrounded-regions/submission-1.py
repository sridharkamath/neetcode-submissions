class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows=len(board)
        cols=len(board[0])
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]

        def dfs(r,c):
            if r<0 or c<0 or r>rows-1 or c>cols-1 or board[r][c]=="X" or board[r][c]=="#":
                return
            
            board[r][c]="#"
            
            for nr,nc in dirs:
                dfs(r+nr,c+nc)
            
        for r in range(rows):
            dfs(r,0)
            dfs(r,cols-1)
        
        for c in range(1,cols-1):
            dfs(0,c)
            dfs(rows-1,c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c]=="O":
                    board[r][c]="X"
                elif board[r][c]=="#":
                    board[r][c]="O"
        