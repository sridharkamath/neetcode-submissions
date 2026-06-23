class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,n in enumerate(nums):
            temp = target - n
            for j,m in enumerate(nums[i+1:]):
                if m==temp:
                    return [i,j+i+1]
        return []