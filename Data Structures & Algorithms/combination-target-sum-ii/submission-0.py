class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res=[]
        curr=[]
        def dfs(i,t):
            if t==0:
                res.append(curr.copy())
                return
            if i==len(candidates) or t<0:
                return
            
            curr.append(candidates[i])
            t-=candidates[i]
            dfs(i+1,t)

            tmp=curr.pop()
            t+=tmp
            j=i
            while j<len(candidates) and candidates[j]==candidates[i]:
                j+=1
            dfs(j,t)

        dfs(0,target)
        return res