class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        prefix=[1]*n
        suffix=[1]*n
        ans=[]
        for i in range(1,n):
            prefix[i]=prefix[i-1]*nums[i-1]
            suffix[n-i-1]=suffix[n-i]*nums[n-i]
        for i in range(n):
            ans.append(prefix[i]*suffix[i])
        return ans
