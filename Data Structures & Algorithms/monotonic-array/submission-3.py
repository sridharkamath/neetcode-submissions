class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True
        else:
            dec=0
            for j in range(1,len(nums)):
                if nums[j]==nums[j-1]:
                    continue
                elif nums[j]>nums[j-1]:
                    if dec==1:
                        return False
                    dec=-1
                elif nums[j]<nums[j-1]:
                    if dec==-1:
                        return False
                    dec=1
            return True