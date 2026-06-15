class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        l=[0]*(len(grid)*len(grid[0]))
        ans=[]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                l[grid[i][j]-1]+=1
        for k,v in enumerate(l):
            if v==2:
                ans.insert(0,k+1)
            if v==0:
                ans.append(k+1)
        return ans