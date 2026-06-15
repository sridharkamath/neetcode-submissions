class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans=[]
        i=1
        for j in range(len(nums)):
            if i not in nums:
                ans.append(i)
            i+=1
        return ans