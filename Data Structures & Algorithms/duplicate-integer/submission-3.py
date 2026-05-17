class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # for i in range(len(nums)-1):
        #     curr=nums[i]
        #     if curr in nums[i+1:]:
        #         return True
        # return False
        # too inefficient code above
        # temp=[]
        # for i in range(len(nums)):
        #     if nums[i] in temp:
        #         return True
        #     else:
        #         temp.append(nums[i])
        # return False
        # above code also very inefficient
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i-1]==nums[i]:
                return True
        return False
