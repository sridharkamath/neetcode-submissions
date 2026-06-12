class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max=nums[0]
        sum=nums[0]
        for i in range(len(nums)-1):
            if nums[i+1]>nums[i]:
                sum+=nums[i+1]
                if sum>=max:
                    max=sum
            else:
                sum=nums[i+1]
        return max