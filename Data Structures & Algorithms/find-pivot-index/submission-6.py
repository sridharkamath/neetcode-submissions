class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n=len(nums)
        tsum=sum(nums)
        lsum=0
        for i in range(n):
            rsum=tsum-lsum-nums[i]
            if lsum==rsum:
                return i
            lsum+=nums[i]
        return -1