class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        chosen = [False]*len(nums)
        curr = []
        def dfs(chosen):
            if len(curr)==len(nums):
                res.append(curr.copy())
                return

            for i in range(len(nums)):
                if chosen[i]:
                    continue

                curr.append(nums[i])
                chosen[i] = True
                dfs(chosen)

                curr.pop()
                chosen[i] = False
        dfs(chosen)
        return res