class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []
        def dfs(i,t):
            if i==len(nums) or t<0:
                return
            if t == 0:
                res.append(curr.copy())
                return
            
            curr.append(nums[i])
            t = t - nums[i]
            dfs(i,t)

            tmp = curr.pop()
            t+=tmp

            dfs(i+1,t)


        dfs(0,target)
        return res