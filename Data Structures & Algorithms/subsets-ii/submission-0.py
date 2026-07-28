class Solution:
    def subsetsWithDup(self, nums: List[int]):
        nums.sort()

        res = []
        curr = []

        def dfs(i):
            if i == len(nums):
                res.append(curr.copy())
                return

            # Include nums[i]
            curr.append(nums[i])
            dfs(i + 1)
            curr.pop()

            # Skip all duplicates
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            # Exclude nums[i]
            dfs(i + 1)

        dfs(0)
        return res