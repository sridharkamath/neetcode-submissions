class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans=[]
        i=1
        l=len(nums)
        for j in range(l):
            if i not in nums:
                ans.append(i)
                i+=1
                continue
            i+=1
        return ans