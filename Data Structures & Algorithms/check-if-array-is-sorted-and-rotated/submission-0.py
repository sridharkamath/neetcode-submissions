class Solution:
    def check(self, nums: List[int]) -> bool:
        breaks=0
        n=len(nums)
        for i in range(n):
            j=(i+1)%n
            if nums[j]<nums[i]:
                breaks+=1
                if breaks==2:
                    return False
        return True
