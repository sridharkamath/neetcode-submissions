class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        c=Counter(nums)
        for _,v in c.items():
            if v & 1 == 1:
                return False
        return True