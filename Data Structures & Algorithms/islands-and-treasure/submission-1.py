class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        lvl = 0
        q = deque()
        visited = set()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==0:
                    q.append((i,j,lvl))
        while q:
            r,c,lvl = q.popleft()
            if (r,c) not in visited:
                grid[r][c] = lvl
                visited.add((r,c))
                if (r+1)<rows:
                    if (r+1,c) not in visited and grid[r+1][c]!=-1:
                        q.append((r+1,c,lvl+1))
                if (c+1)<cols:
                    if (r,c+1) not in visited and grid[r][c+1]!=-1:
                        q.append((r,c+1,lvl+1))
                if (r-1)>=0:
                    if (r-1,c) not in visited and grid[r-1][c]!=-1:
                        q.append((r-1,c,lvl+1))
                if (c-1)>=0:
                    if (r,c-1) not in visited and grid[r][c-1]!=-1:
                        q.append((r,c-1,lvl+1))

                            
                        
                            


