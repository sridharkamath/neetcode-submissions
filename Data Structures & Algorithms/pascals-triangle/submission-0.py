class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==1:
            return [[1]]
        else:
            ans=[[1],[1,1]]
            for i in range(2,numRows):
                curr=[1,1]
                for j in range(1,i):
                    curr.insert(j,ans[i-1][j-1]+ans[i-1][j])
                ans.append(curr)
            return ans