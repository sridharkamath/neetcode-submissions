class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i,j=0,1
        while j<len(nums):
            aim=target-nums[i]
            while j!=len(nums):
                if nums[j]==aim: return [i,j]
                j+=1
            i=i+1
            j=i+1