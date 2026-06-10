class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        nums.append(0)
        n=len(nums)
        tsum=sum(nums)
        lsum,rsum=0,tsum-nums[0]
        for i in range(n-1):
            if lsum==rsum:
                return i
            else:
                lsum+=nums[i]
                rsum-=nums[i+1]
        return -1