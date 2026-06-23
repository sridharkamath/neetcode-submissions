class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        c=Counter(nums)
        for n,v in c.items():
            if v>1:
                return True
        return False